from django.shortcuts import render
from django.shortcuts import HttpResponse

def about(request):
    # return HttpResponse("hi dear !")
    return render(request, 'about.html')

def home(request):
    # return HttpResponse("there is home page of my website...")
    return render(request, 'Home.html')