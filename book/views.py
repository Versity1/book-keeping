from django.shortcuts import render
from .models import product
# Create your views here.
def home(request):
    return render(request, 'index.html')

def products(request):
    products = product.objects.all()
    context = {'products': products}
    return render(request, 'products.html', context)