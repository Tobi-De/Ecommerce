from django.shortcuts import render

from .models import Item


def home(request):
    context = {
        "items": Item.objects.all()
    }
    return render(request, "pages/home.html", context)


def checkout(request):
    return render(request, "pages/checkout.html")


def product(request):
    return render(request, "pages/product.html")
