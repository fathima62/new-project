from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'jobseeker/login.html')

def search(request):
        return render(request,'jobseeker/job_search.html')
def details(request):
    return render(request,'jobseeker/job_details.html')


    


