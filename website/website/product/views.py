import dataclasses
from urllib import request
from django.shortcuts import render, HttpResponse
from product.models import about
from product.models import contact
from .models import *
# Create your views here.


def home(request):
   info = CompanyInformation.objects.first()
   products = Product.objects.all()
   
   data ={
      
      'info':info,
      'products':products
   }
   
   return render(request, 'home.html',data)

def about(request):
    about_info = about.objects.all().first()
    
    data = {
        'about_info': about_info,
    }
    return render(request, 'about.html', data)


def contact(request):
   
   if request.method =='POST':
       
      name  = request.POST.get('name')
      email  = request.POST.get('email')
      comment  = request.POST.get('comment')
      new_contact = contact(name=name, email=email, comment=comment)
      new_contact.save()

      return HttpResponse("<h1> THANKS FOR CONTACT US</h1>")
   return render(request, 'contact.html')

def product(request):
    info = CompanyInformation.objects.first()
    products = Product.objects.all()
   
    data ={
      
      'info':info,
      'products':products
   }
    return render(request, 'product.html',data)