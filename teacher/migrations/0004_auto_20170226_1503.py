# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0003_remove_management_start'),
    ]

    operations = [
        migrations.AddField(
            model_name='management',
            name='hour',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='management',
            name='minute',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
