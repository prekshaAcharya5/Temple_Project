from django.urls import path
from .views.auth_views import register,login
#from .views.main_views import

urlpatterns = [
    path("register",register),
    path("login",login)
]
