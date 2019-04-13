from django.conf.urls import url
from django.contrib import admin
from student import views

urlpatterns = [
		url(r'^(?P<str>.+)/submit_student/$', views.submit_student , name='submit_student'),
		url(r'^(?P<str>.+)/$', views.student),		
]