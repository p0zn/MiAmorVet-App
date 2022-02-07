from django import views
from django.contrib import admin
from django.urls import path
from . import views


app_name = "pet"

urlpatterns = [
  path('dashboard/', views.dashboard, name="dashboard"),
  path('addpet/', views.addPet, name="addpet"),
  path('pet/<int:id>', views.detail, name="detail"),
  path('update/<int:id>', views.updatePet, name="update"),
  path('delete/<int:id>', views.deletePet, name="delete"),
  path('', views.pets, name="pets"),

]


