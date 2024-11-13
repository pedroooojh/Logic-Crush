from django.urls import path
from app_truth_crush import views

urlpatterns = [
    path('', views.index, name='index'),
    path('nivel1/', views.nivel1, name='nivel1'),
    path('nivel2/', views.nivel2, name='nivel2'),
    path('nivel3/', views.nivel3, name='nivel3'),
    path('atualizar_pontuacao/', views.atualizar_pontuacao, name='atualizar_pontuacao'),
]
