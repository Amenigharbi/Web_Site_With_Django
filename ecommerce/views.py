from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import *
from django.core.paginator import Paginator
# Create your views here.

def product_list(request):
    product_list=Product.objects.all()

    paginator = Paginator(product_list,2)
    page_number = request.GET.get("page")
    product_list = paginator.get_page(page_number)

    return render (request ,'Product/product_list.html',{'pro':product_list})


def product_detail(request,slug):
    product_de=Product.objects.get(proSlug=slug)
    context={'prod':product_de}
    return render(request,'Product/prod_detail.html',context)
