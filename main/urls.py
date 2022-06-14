from django.urls import path
from . import views

urlpatterns = [

    path('registr/', views.registr, name = 'registr'),


]