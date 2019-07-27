from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('create', views.create),
    path('delete/<int:pk>', views.delete),
    path('edit/<int:pk>', views.edit),
]