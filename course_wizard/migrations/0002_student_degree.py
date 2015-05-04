# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course_wizard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='degree',
            field=models.ForeignKey(to='course_wizard.Degree', null=True),
        ),
    ]
