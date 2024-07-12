"""agriculture URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from agriculture import views as mainView
from admins import views as admins
from farmers import views as usr

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", mainView.index, name="index"),
    # path("index/", mainView.index, name="index"),
    path("Adminlogin/",mainView.AdminLogin,name="AdminLogin"),
    path("UserLogin/", mainView.UserLogin, name="UserLogin"),
    path("UserRegister/", mainView.UserRegister, name="UserRegister"),
    
    
    
    #farmers
    path("UserRegisterActions/", usr.UserRegisterActions, name="UserRegisterActions"),
    path("UserLoginCheck/", usr.UserLoginCheck, name="UserLoginCheck"),
    path("UserHome/", usr.UserHome, name="UserHome"),
    path('cropdata/', usr.cropdata,name='cropdata'),
    path('cropprice/', usr.cropprice,name='cropprice'),
    
    
    #admin side views
    path("AdminLoginCheck/", admins.AdminLoginCheck, name="AdminLoginCheck"),
    path("AdminHome/", admins.AdminHome, name="AdminHome"),
    path('RegisterUsersView/', admins.RegisterUsersView, name='RegisterUsersView'),
    path('ActivaUsers/', admins.ActivaUsers, name='ActivaUsers'),
    path('DeleteUsers/', admins.DeleteUsers, name='DeleteUsers'),
    path('storecsvdata/', admins.storecsvdata, name='storecsvdata'),
    path('knnalgo/',admins.knnalgo,name='knnalgo'),
    path('rf1/',admins.rf1,name='rf1'),
    path('lstmtest/',admins.lstmtest,name='lstmtest'),
    
    
]
from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)