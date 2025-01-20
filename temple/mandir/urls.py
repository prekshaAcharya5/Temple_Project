from django.urls import path
from .views.auth_views import register,login
from .views.main_views import aboutus,beadoner,doner,event,gallery,home,member,notice

urlpatterns = [
    path("register",register),
    path("login",login),
    path("aboutus",aboutus),
    path("beadoner",beadoner),
    path("doner",doner),
    path("event",event),
    path("gallery",gallery),
    path("",home),
    path("member",member),
    path("notice",notice)
]
