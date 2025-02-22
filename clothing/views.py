from django.shortcuts import render
from clothing.models import product

# Create your views here.

def clothing(request):
    pro_img = product.objects.all()
    return render(request, 'clothing/fashion.html',{'pro_img': pro_img})