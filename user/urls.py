from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="main"),
    path('register/',views.register,name="register"),
    path('viewprofile/',views.viewprofile,name="show profile"),
    path('dashboard/',views.dash,name="dashboard"),
    path('acknow/',views.acknow,name="acknow"),
]