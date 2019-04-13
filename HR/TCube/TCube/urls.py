"""TCube URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),  
    url(r'^fdp/',include('FDPmanager.urls',namespace='FDP')),
    url(r'^$',views.homePage,name='home'),
    url(r'^registration/', include('registration.urls', namespace='registration')),
    url(r'^manageRCCapacity/', include('manageRCCapacity.urls', namespace='manageRCCapacity')),
    url(r'^attendance/', include('attendance_module.urls', namespace = "attendance") ),
    url(r'^certification/', include('certificate_module.urls', namespace = "certification") ),
    url(r'^email_content/$', "email_content.views.show_templates",name="email_content"),
    url(r'^page_manage/$', "page_manage.views.show_pagecontent", name="show_pagecontent"),
    url(r'^page_manage/update/$', "page_manage.views.update_pagecontent",name="update_pagecontent"),    
    url(r'^role_manage/', include("role_manage.urls",namespace="role_manage")),
    url(r'^faculty_pool/', include("faculty_pool.urls",namespace="faculty_pool")),
    url(r'^statusManagement/',include("statusManagement.urls",namespace="statusManagement")),
	#url(r'^report/', include("workshop_status_summary.urls",namespace="report")),
    url(r'^allworkshops/',include("list_workshop.urls",namespace="allworkshops")),
    url(r'^ourteam/',views.ourteam,name='ourteam'),

]
