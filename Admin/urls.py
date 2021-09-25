from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('viewprofile/',views.viewprofile,name="show profile"),
    path('viewnotice/',views.viewnotice,name="show notice"),
    path('addnotice/',views.__addNotice__,name="add notice"),
]
