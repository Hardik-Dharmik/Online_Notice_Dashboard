from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="main"),
    # path('notice/',views.notice,name="notice"),
    path('user/',include('user.urls')),
    path('Admin/',include('Admin.urls')),
    path('register/',views.register,name="register"),
    path('show/',views.viewprofile,name="profile"),
    path('login/',views.__login__,name="login"),
    path('logout/',views.__logout__,name="logout"),
    path('dashuser/',views.dash_user,name="dash_user"),
    path('dashadmin/',views.dash_admin,name="dash_admin"),
    # path('logout/',views.__logout__,name="logout"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

