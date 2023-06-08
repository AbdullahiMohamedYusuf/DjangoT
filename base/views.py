from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Shoe, Purchase


# Create your views here.

def home(request):
    items = Shoe.objects.all()
    context = {"items": items}
    for shoe in items:
        print(shoe.name)
    print(items)
    return render(request, 'base/item.html', context)

def rooms(request, pk):
    item = Shoe.objects.get(id=pk)
    context = {"shoe": item}
    if request.method == 'POST':
        Purchase.objects.create(shoe=item)

    
  
    return render(request, 'base/room.html', context)

def cart(request):
    item = Purchase.objects.get()
    context = {"item": item}
    print(item)
    return render(request, 'base/cart.html', context)
