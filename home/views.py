from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'home.html') 
    #return HttpResponse("Welcome page of the AJ Bike Modification")

def about(request):
    #return HttpResponse("About page of the AJm Bike Modification")
    return render(request, 'about.html') 

def gallery(request):
    #return HttpResponse("contact page of the AJ Bike Modification")
    return render(request, 'gallery.html') 

def services(request):
    #return HttpResponse("services page of the AJ Bike Modification")
    return render(request, 'services.html') 
    

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')
    
    