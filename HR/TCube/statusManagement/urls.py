from django.conf.urls import url
from django.contrib import admin
from statusManagement import views

urlpatterns = [
		url(r'^changeStatus/$',views.changeStatus),
		url(r'^statusManage/$', views.status,name='status'),
		url(r'^statusManage/(\d+)/(\d+)/(\d+)/$',views.status_manage,name='statusmanage'),
		url(r'^viewRCCapacity/(\d+)/(\d+)/$',views.viewRCCapacity,name='viewRCCapacity'),
		url(r'^sendMail/$',views.sendMail,name='sendMail'),
		url(r'^sendMailCancel/$',views.sendMailCancel,name='sendMail_cancel'),
		url(r'^loadLastRC/$',views.loadLastRC,name='loadLastRC'),
		url(r'^photo/(\d+)/$',views.showPhoto,name='showPhoto'),
		url(r'^photo/(\d+)/(\d+)/$',views.showLetter,name='showLetter'),
]
