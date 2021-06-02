# from django.contrib import admin
from django.urls import path
from app1.views import view, index, common

urlpatterns = [
    path('Data/', view, name='calc'),
    path('', index, name='home'),
    path('common', common, name='common'),

]
