# This is where your views go :)
#from django.views.generic.list import ListView
#from django.views.generic.detail import DetailView
#from django.views.generic.edit import CreateView, UpdateView
#from django.contrib import messages
from django.http import JsonResponse

from course_wizard.models import *
from scheduling.schedule import make_schedule
from scheduling.course import Course as schedule_course

def list_of_courses(request):
    # If the schedule.Course.__courses_by_crn hasn't been populated, populate it
    if schedule_course.initialized == False:
        for course in Course.objects.all():
            course.to_schedule_course()
    # Get the completed and required courses
    completed = get_user_completed_courses(request.user)
    required = get_user_required_courses(request.user)
    schedule = make_schedule(required, completed)

    ret = []

    if schedule == False:
        raise Exception("Cannot construct course schedule")

    for course in schedule:
        for day in course.model.timeslot.days.all():
            ret += [{
                'title': course.CRN,
                'start': day.start_time,
                'end': day.end_time,
                'day': day.day
            }]

    return JsonResponse(ret, safe=False)
