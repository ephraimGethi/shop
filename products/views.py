from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Product
# Create your views here.


def index(request):
    products = Product.objects.all()
    return render(request,'index.html',{"products":products})

def new(request):
    return HttpResponse('new products we have in our site')

