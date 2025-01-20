from django.urls import path
from .views.auth_views import register,login
from .views.main_views import about_us,be_a_doner,doner,event,gallery,home,committe_member,notice,committe,create_committee_member,add_committe

urlpatterns = [
        path("register",register),
        path("login",login),
        path("aboutus",about_us),
        path("beadoner",be_a_doner),
        path("doner",doner),
        path("event",event),
        path("gallery",gallery),
        path("",home),
        path('committe',committe),
        path('add_member/',create_committee_member,name='add_member'),
        path("committe_member",committe_member,name='committe_member'),
        path('add_committe/',add_committe,name="add_committe"),
        path("notice",notice)
    ]
