# This is where you can add stuff to the admin view
from django.contrib import admin

# ie,
# admin.site.register(User, UserAdmin)

from models import *

admin.site.register(Student)
admin.site.register(StudentCourse)
admin.site.register(Degree)
admin.site.register(DegreeRequirement)
admin.site.register(DegreeRequirementOption)
admin.site.register(Course)
admin.site.register(Timeslot)
