import os
from django.conf import settings
from django.shortcuts import render

def index(request):
    return render(request, 'app_truth_crush/index.html')

def nivel1(request):
    return render(request, 'app_truth_crush/nivel1.html')

def nivel2(request):
    return render(request, 'app_truth_crush/nivel2.html')

def nivel3(request):
    return render(request, 'app_truth_crush/nivel3.html')