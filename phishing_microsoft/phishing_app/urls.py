from django.urls import path
from . import views

urlpatterns = [
    path('connexion/', views.page_connexion, name='page_connexion'),  # page de connexion
    path('sondage/', views.sondage, name='sondage'),  # page de sondage
    path('tentatives/', views.liste_tentatives, name='liste_tentatives'),  # liste des tentatives
]