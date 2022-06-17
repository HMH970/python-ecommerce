from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # return HttpResponse('<h1>Home</>')
    return render(request, 'home.html')
def aboutPage(request):
    # return HttpResponse('<h1>About Us</>')
    return render(request, 'about.html')
# Create your views here.
