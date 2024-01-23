from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from home.models import About
from django.contrib import messages



def home(request):
    
    if request.method == "POST":
        name = request.POST.get('name')
        number = request.POST.get('number')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        about = About(name=name, number=number, email=email, desc=desc, date=datetime.today())
        about.save()
        messages.success(request, "Your message has been send!")
        

    return render(request, "index.html")

def demo(request):
    return HttpResponse("Hello")

# Create your views here.
