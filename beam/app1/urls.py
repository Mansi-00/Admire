# from django.contrib import admin
from django.urls import path
from app1.views import view, index

urlpatterns = [
    path('Data/', view),
    path('', index),

]
