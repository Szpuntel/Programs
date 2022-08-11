from django.contrib import admin
from django.urls import path, include
from django.views import *
from authentication import views
from Produkty.views import *



urlpatterns = [
    path('login/', views.login_auth, name='login'),
    path('signup/', views.signup_auth, name='signup'),
    path('profile/', views.profile, name='profile'),
    path("logout/", views.logout_auth, name= "logout"),

]