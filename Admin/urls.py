from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('viewprofile/',views.viewprofile,name="show profile"),
    path('viewnotice/',views.viewnotice,name="show notice"),
    path('addnotice/',views.__addNotice__,name="add notice"),
    path('updatenotice/',views.updatenotice,name="update notice"),
    path('updatenoticeindb/',views.updatenotice_in_db,name="actual update notice"),
    path('deletenotice/',views.deletenotice,name="actual delete notice"),
    path('student/',views.student,name="student"),
    path('<int:sno>',views.viewinfo,name="view info"),
    path('<str:username>',views.viewstudent,name="view student"),
]
