from django.urls import path
from . import views

urlpatterns = [
    path('connexion/', views.page_connexion, name='page_connexion'),  # page de connexion
    path('tentatives/', views.liste_tentatives, name='liste_tentatives'),  # liste des tentatives
    path('merci/', views.merci, name='merci'),  # page de remerciement
]