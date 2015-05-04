# This is where the models go!
from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings

from scheduling.course import Course as schedule_course
from scheduling.course import Timeslot as schedule_timeslot
from scheduling.requirement import Requirement as schedule_requirement

def get_user_completed_courses(user):
    # Return a static list for now
    ret = []
    for course in user.student_profile.courses.all():
        ret += [course.crn]
    return ret

def get_user_required_courses(user):
    # Return a static list for now
    #return ["CSCI-1100","CSCI-1200","CSCI-2200","CSCI-2500","CSCI-2300","CSCI-2600","CSCI-4430","CSCI-4210"]
    ret = []
    for requirement in user.student_profile.degree.degreerequirement_set.all():
        req = []
        for r in requirement.degreerequirementoption_set.all():
            req += [r.crn]
        ret += [schedule_requirement(req)]
    return ret

# Using the user: user = models.ForeignKey(settings.AUTH_USER_MODEL)
class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="student_profile")
    rin = models.IntegerField()
    courses = models.ManyToManyField('course_wizard.Course', through='course_wizard.StudentCourse')
    degree = models.ForeignKey('course_wizard.Degree', null=True)

    when_created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "%d -- %s" % (self.rin, self.user.__unicode__())

class StudentCourse(models.Model):
    student = models.ForeignKey('course_wizard.Student')
    course = models.ForeignKey('course_wizard.Course')

    grade_points = models.FloatField()

    def __unicode__(self):
        return "%s taking %s" % (self.student.__unicode__(), self.course.__unicode__())

class Degree(models.Model):
    name = models.CharField(max_length=255)
    year = models.IntegerField()

    def __unicode__(self):
        return "%s, %s" % (self.name, self.year)

class DegreeRequirement(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    degree = models.ForeignKey('course_wizard.Degree')

    def __unicode__(self):
        return "%s requires %s" % (self.degree.__unicode__(), self.name)

class DegreeRequirementOption(models.Model):
    requirement = models.ForeignKey('course_wizard.DegreeRequirement')
    crn = models.CharField(max_length=16)

    def __unicode__(self):
        return self.crn

class Course(models.Model):
    crn = models.CharField(max_length=255)
    credit_hours = models.FloatField()

    # We can't store this as foreignkey because Courses have timeslot attached
    prereqs = models.CharField(max_length=255, null=True, blank=True)
    timeslot = models.ForeignKey('course_wizard.Timeslot')

    title = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return "%s @ %s" % (self.crn, self.timeslot.__unicode__())

    def to_schedule_course(self):
        ret = schedule_course(self.crn, self.timeslot.to_schedule_timeslot(),
            self.prereqs.split(','), self.credit_hours)
        ret.model = self
        return ret

    @staticmethod
    def from_schedule_course(course, semester=None):
        # First make the timeslot
        prereqs = None
        if course.prereqs != '':
            prereqs = ','.join(course.prereqs)
        timeslot = Timeslot.from_schedule_timeslot(course.timeslot, semester)
        return Course(crn=course.CRN, credit_hours=course.credit_hours,
            prereqs=prereqs, timeslot=timeslot, title=course.kwargs['course_title'])

class Timeslot(models.Model):
    semester = models.CharField(max_length=4)

    def __unicode__(self):
        ret = self.semester + "; "
        for day in self.days.all():
            ret += day.__unicode__()
        return ret

    def to_schedule_timeslot(self):
        day_times = {}
        for day in self.days.all():
            day_times.update(day.to_object())
        return schedule_timeslot(self.semester, day_times)

    @staticmethod
    def from_schedule_timeslot(timeslot, semester=None):
        if semester != None:
            timeslot.semester = semester
        ts = Timeslot(semester=timeslot.semester)
        ts.save()
        for day in timeslot.day_time:
            dt = DayTime(timeslot=ts, day=day, start_time=timeslot.day_time[day][0],
                end_time=timeslot.day_time[day][1])
            dt.save()
        return ts

class DayTime(models.Model):
    timeslot = models.ForeignKey('course_wizard.Timeslot', related_name='days')
    day = models.CharField(max_length=1)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __unicode__(self):
        return "%s %s-%s" % (self.day, self.start_time, self.end_time)

    def to_object(self):
        start_time = "%02d:%02d" % (self.start_time.hour, self.start_time.minute)
        end_time = "%02d:%02d" % (self.end_time.hour, self.end_time.minute)

        return {self.day: [start_time, end_time]}
