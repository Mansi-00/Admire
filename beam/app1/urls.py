# from django.contrib import admin
from django.urls import path
from app1.views import view, index, common, login, register

urlpatterns = [
    path('Data/', view, name='calc'),
    path('', index, name='home'),
    path('common', common, name='common'),
    path('login', login, name='login'),
    path('register', register, name='register'),

]
