from django.contrib import admin
from django.urls import path
from home import views

urlpatterns =[
path("", views.index,name='index.html'),    
path("index", views.index,name='index.html'),

path("signup", views.signup, name='signup.html'),
path("login", views.login, name='login.html'),
# path("secret", views.secret, name='secret.html'),
path("second", views.second, name='second.html'),
path("dashboard", views.Dashboard, name='dashboard.html'),
path("calculate", views.calculate, name='dashboard.html')
]
