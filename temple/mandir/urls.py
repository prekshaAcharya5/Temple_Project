from django.urls import path
from .views.auth_views import register,login
from .views.main_views import about_us,be_a_doner,doner,event,gallery,home,committe_member,notice,committe,add_member

urlpatterns = [
        path("register",register),
        path("login",login),
        path("aboutus",about_us),
        path("beadoner",be_a_doner),
        path("doner",doner),
        path("event",event),
        path("gallery",gallery),
        path("",home),
        path('',committe),
        path('addmember/',add_member),
        path("member",committe_member),
        path("notice",notice)
    ]
