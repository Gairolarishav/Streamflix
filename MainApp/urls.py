from django.contrib import admin
from django.urls import path
from django.urls import include
from MainApp import views

urlpatterns = [
    path('Signin', views.loginpage,name='signin'),
    path('Signup', views.Signup,name='signup'),
    path('', views.Homepage,name='homepage'),
    path('Feature', views.feature,name='feature'),
    path('Aboutus', views.aboutus,name='aboutus'),
    path('Privacy', views.privacy,name='privacy'),
    path('Termsandservices', views.termsandservices,name='termsandservices'),
]
