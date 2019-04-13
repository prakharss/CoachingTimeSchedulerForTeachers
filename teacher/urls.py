from django.conf.urls import url
from django.contrib import admin
from teacher import views

urlpatterns = [
		url(r'^$',views.teacher),
		url(r'^clear/$',views.clear),
		url(r'^submit/$',views.submit_teacher,name='submit_teacher'),		
]