from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'employers/login.html')
def home(request):
    return render(request,'employers/home.html')