from django.conf.urls import url
from django.contrib import admin
from manageRCCapacity import views

urlpatterns = [
	url(r'^$', views.RCCapacity, name='RCCapacity'),
	url(r'^sendMail/$',views.sendMail,name='sendMail'),
	url(r'^sendMail_RCCapacity/$',views.sendMail_RCCapacity,name='sendMail_RCCapacity'),
	url(r'^message.html/$',views.message),
	url(r'^updateMessage.html/$',views.updateMessage),
	#url(r'^displayRCCapacityDetails.html/(\d+)/(\d+)/',views.displayRCCapacityDetails,name='displayRCCapacityDetails'),
	#url(r'^RCCapacityDetails.html/(\d+)/(\d+)/$',views.rCCapacityDetails),
	url(r'^RCCInterface.html/(\d+)/(\d+)/$',views.rCCapacityDetails),
	url(r'^RCCInterface.html/$',views.rCCInterface,name='RCCInterface'),
	url(r'^addRC/(\d+)/$',views.addRC,name='addRC'),
	url(r'^updateRCSuccess.html/(?P<wsid>\d+)/(?P<rcId>\d+)/$',views.updateRCSuccess,name='updateRCSuccess'),
	#url(r'^updateRCCapacity.html/',views.updateRCCapacity,name='updateRCCapacity'),
	url(r'^updateRCCapacity.html/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/$',views.updateRC,name='updateRC'),
	url(r'^manageRC.html/(\d+)/viewRCCapacity/(\d+)/$',views.viewRC,name='view'),
	url(r'^manageRC.html/(\d+)/addNewRC/$',views.add,name='add'),
	url(r'^manageRC.html/$',views.manage,name='manage'),
	#url(r'^manageRC.html/(?P<workshopId>\d+)/',views.manageRC,name='manageRCCapacity'),
	url(r'^manageRC.html/(\d+)/$',views.manageRC,name='manageRCCapacity'),
	url(r'^deleteRC.html/(\d+)/(\d+)/$',views.deleteRC,name='deleteRC'),
	url(r'^capacityFilled/$',views.capacityFilled,name='capacityFilled'),
	url(r'^fillSeats/$',views.fillSeats,name='fillSeats'),
	url(r'^declineRC/$',views.declineRC,name='declineRC'),
	url(r'^saveDeclinedRC/$',views.saveDeclinedRC,name='saveDeclinedRC'),
	url(r'^RCCInterface/(?P<rcid>\d+)/(?P<wsid>\d+)/$', views.manageparticipants, name='manageparticipants'),
	url(r'^viewRCParticipants/(\d+)/(\d+)/(\d+)/$', views.viewRCParticipants, name='viewRCParticipants'),
	url(r'^viewProgramSchedule/(\d+)/$', views.viewProgramSchedule, name='viewProgramSchedule'),
	url(r'^changeStatus/$',views.changeStatus,name='changeStatus'),
    	url(r'^admin/$', admin.site.urls),
]
