from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.home),
    path('create', views.create),
    path('<int:pk>', views.detail),
    path('delete/<int:pk>', views.delete),
    path('edit/<int:pk>', views.edit),
]