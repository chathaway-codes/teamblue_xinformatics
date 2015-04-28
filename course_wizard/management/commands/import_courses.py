from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from optparse import make_option

from scheduling.load_available_courses import load_available_courses
from course_wizard.models import *

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_filename')
        parser.add_argument('--semester', default=None)

    def handle(self, *args, **options):
        courses = load_available_courses(options['csv_filename'])
        for course in courses:
            c = Course.from_schedule_course(course, options['semester'])
            c.save()
