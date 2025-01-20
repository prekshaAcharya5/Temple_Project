from django.urls import path
from .views.auth_views import register,login
from .views.main_views import aboutus,add_donor,donor_form,event,gallery,home,member,notice,create_committee_member,edit_donor

urlpatterns = [
    path("register",register),
    path("login",login),
    path("aboutus",aboutus),
    path("beadonor",donor_form),
    path("adddonor",add_donor),
    path("editdonor/<int:donor_id>/",edit_donor,name="edit_donor"),
    path("event",event),
    path("gallery",gallery),
    path("",home,name="home"),
    path("member",member),
    path("createcommittemember",create_committee_member),
    path("notice",notice)
]
