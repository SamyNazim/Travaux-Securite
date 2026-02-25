from django.urls import path
from . import views

urlpatterns = [
    path('', views.page_connexion, name="login"),
    path('rapport/', views.liste_tentatives, name="rapport"),
]