from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(CategProd)
admin.site.register(Product_Alternative)
admin.site.register(Product_Accessoires)