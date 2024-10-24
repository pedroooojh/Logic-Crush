from django.urls import path
from app_truth_crush import views

urlpatterns = [
    path('',views.home,name='home'),
]
