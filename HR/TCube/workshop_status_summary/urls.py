from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', "workshop_status_summary.views.show_reports",name="show_reports"),
    url(r'^workshop_status_summary/$', "workshop_status_summary.views.show_w_s_s"),
    url(r'^workshop_diversity/$', "workshop_status_summary.views.show_w_d"),
    url(r'^remote_centre_summary/$', "workshop_status_summary.views.show_rc_wise"),
    url(r'^state_wise_summary/$', "workshop_status_summary.views.show_state_wise"),
    url(r'^get_Invite_Not_RegData/$', "workshop_status_summary.views.invite_not_register"),
    url(r'^get_Invite_Not_RegData/enable_disable/$', "workshop_status_summary.views.enable_disable"),    
    url(r'^get_Login_Not_RegData/$', "workshop_status_summary.views.login_not_register"),
    url(r'^total_ws_by_participant_wise/$', "workshop_status_summary.views.ws_p_wise",name="total_ws_by_participant_wise"),
    url(r'^total_ws_by_institute_wise/$', "workshop_status_summary.views.ws_i_wise",name="total_ws_by_institute_wise"),
]
