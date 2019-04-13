from django.conf.urls import include, url
from login.views import *
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
	    url(r'^$', auth_views.login),
	    url(r'^logout/$', logout_page),
	    url(r'^accounts/login/$', auth_views.login), # If user is not login it will redirect to login page
	    url(r'^register/$', register),
	    url(r'^register/success/$', register_success),
	    url(r'^teacher/', include('teacher.urls', namespace="teacher")),
	    url(r'^student/', include('student.urls', namespace='student')),
	    url(r'^admin/',admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
