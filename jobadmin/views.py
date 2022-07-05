from django.shortcuts import render

# Create your views here.
def admin_login(request):
    return render(request,'jobadmin/login.html')
def admin_signup(request):
    return render(request,'jobadmin/signup.html')
def emplyers_lst(request):
    return render(request,'jobadmin/view_employers.html')
    