# This is where your views go :)
#from django.views.generic.list import ListView
#from django.views.generic.detail import DetailView
#from django.views.generic.edit import CreateView, UpdateView
#from django.contrib import messages
import json
from django.contrib.auth import authenticate, login
from django.http import JsonResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from course_wizard.models import *
from scheduling.schedule import make_schedule
from scheduling.course import Course as schedule_course

@csrf_exempt
def api_login(request):
    if request.method != "POST":
        return HttpResponseForbidden()

    # Try to login
    response = json.loads(request.body)
    username = response['username']
    password = response['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return JsonResponse({'login': 'success'})
        else:
            return HttpResponseForbidden()
    else:
        return HttpResponseForbidden()

def list_student_info(request):
    # Returns information about the currently logged in user
    ret = {}
    ret['name'] = "%s %s" % (request.user.first_name, request.user.last_name)
    ret['rin'] = request.user.student_profile.rin
    ret['degree'] = request.user.student_profile.degree.__unicode__()
    ret['courses'] = []
    ret['required'] = []

    def get_grade(points):
        if points == 4.0:
            return 'A'
        if points == 3.0:
            return 'B'
        if points == 2.0:
            return 'C'
        if points < 2.0:
            return 'F';

    for course in request.user.student_profile.courses.all():
        sc = StudentCourse.objects.get(course=course, student=request.user.student_profile)
        ret['courses'] += [{
            'crn': course.crn,
            'title': course.title,
            'grade': get_grade(sc.grade_points)
        }]

    for requirement in request.user.student_profile.degree.degreerequirement_set.all():
        sc = {}
        sc['name'] = requirement.name
        sc['options'] = []
        for option in requirement.degreerequirementoption_set.all():
            sc['options'] += [option.crn]
        ret['required'] += [sc]

    return JsonResponse(ret)

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
