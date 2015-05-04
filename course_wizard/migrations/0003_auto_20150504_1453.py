# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('course_wizard', '0002_student_degree'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='title',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='user',
            field=models.OneToOneField(related_name='student_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
