from django.shortcuts import render

def home(request):
    return render(request,'Truth Crush/home.html')
