from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Management(models.Model):
	userid = models.CharField(max_length=150, blank=True, null=True)
	day = models.CharField(max_length=150, blank=True, null=True)
	slotid = models.IntegerField(blank=True, null=True)
	time = models.CharField(max_length=150, blank=True, null=True)
	studentname = models.CharField(max_length=150, blank=True, null=True)
	studentemail = models.CharField(max_length=100, blank=True, null=True)
	bookingstatus = models.IntegerField(blank=True, null=True)
    

	def __unicode__(self):
		return self.userid