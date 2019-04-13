# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='management',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('userid', models.CharField(max_length=150, null=True, blank=True)),
                ('day', models.CharField(max_length=150, null=True, blank=True)),
                ('slotid', models.IntegerField(null=True, blank=True)),
                ('start', models.DateTimeField()),
                ('studentname', models.CharField(max_length=150, null=True, blank=True)),
                ('studentemail', models.CharField(max_length=100, null=True, blank=True)),
                ('bookingstatus', models.IntegerField(null=True, blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='hi',
        ),
    ]
