from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # TemplateView + Login
    #url(r'^$', login_required(TemplateView.as_view(template_name="home.html")), {}, 'home'),
    url(r'^api/courses/$', 'course_wizard.views.list_of_courses', name='api-courses'),
    url(r'^api/student/$', 'course_wizard.views.list_student_info', name='api-student'),
    url(r'^api/login/$', 'course_wizard.views.api_login', name='api-login'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
