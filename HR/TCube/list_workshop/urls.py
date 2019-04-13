from django.conf.urls import url
from django.contrib import admin
from list_workshop import views

urlpatterns = [
	url(r'^$', views.allworkshops , name='allworkshop'),
    url(r'^introworkshop/(?P<wsid>\d+)/$', views.introworkshop , name='aboutworkshop'),
    url(r'^download/(?P<wsid>\d+)/$', views.download , name='downloadoption'),
	url(r'^admin/$', admin.site.urls),
]
