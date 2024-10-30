from django.urls import path
from app_truth_crush import views

urlpatterns = [
    path('', views.index, name='index'),
    path('nivel1/', views.nivel1, name='nivel1'),
]
