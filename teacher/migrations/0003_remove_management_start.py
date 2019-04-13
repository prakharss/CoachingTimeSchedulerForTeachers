# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_auto_20170226_1305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='management',
            name='start',
        ),
    ]
