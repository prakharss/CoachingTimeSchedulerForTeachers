# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0004_auto_20170226_1503'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='management',
            name='hour',
        ),
        migrations.RemoveField(
            model_name='management',
            name='minute',
        ),
        migrations.AddField(
            model_name='management',
            name='time',
            field=models.CharField(max_length=150, null=True, blank=True),
        ),
    ]
