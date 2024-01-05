
from django.contrib import admin
from django.urls import path
from . import views 
app_name="ecommerce"
urlpatterns = [
    path('', views.product_list),
    path('one_prod/<slug:slug>', views.product_detail,name='product_detail'),
    
]