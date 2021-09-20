from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="main"),
    path('user/',include('user.urls')),
    path('register/',views.register,name="register"),
    path('show/',views.viewprofile,name="profile"),
    path('login/',views.__login__,name="login"),
    path('logout/',views.__logout__,name="logout")
]

