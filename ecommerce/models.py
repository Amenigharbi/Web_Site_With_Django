from django.db import models
from django.utils.text import slugify 
# Create your models here.


class CategProd(models.Model):
    CatMain_category=models.CharField(max_length=40)
    CatParent=models.ForeignKey('self',on_delete=models.CASCADE,blank=True,null=True,limit_choices_to={'CatParent__isnull':True})
    CatDescription=models.TextField()
    CatImage=models.ImageField(upload_to="proImages/%y/%m/%d",verbose_name="image category ")
    class Meta:
        verbose_name= ("categories")
        verbose_name_plural= ("categories")
        

    def __str__(self):
        return self.CatMain_category

class Product(models.Model):
    Proname=models.CharField(max_length=50,verbose_name="product name",default="name")
    Procategory=models.ForeignKey(CategProd,on_delete=models.CASCADE,blank=True,null=True)
    Prodescription=models.TextField(verbose_name="Description",default="text")
    Price=models.DecimalField(max_digits=4,decimal_places=2)
    ProCost=models.DecimalField(max_digits=4,decimal_places=2)
    ProCreated=models.DateTimeField()
    ProdBrand=models.ForeignKey('settings.Brand',on_delete=models.CASCADE,blank=True,null=True)
    proImage=models.ImageField(upload_to="proImages/%y/%m/%d",verbose_name="image",blank=True,null=True)
    proSlug=models.SlugField(null=True,blank=True)


    def __str__(self):
        return self.Proname
    
    def save(self,*args,**kwargs):
        if not self.proSlug:
            self.proSlug=slugify(self.Proname)
        super(Product,self).save(*args,**kwargs)

    
class ProductImage(models.Model):
    #on delete cascade ken msa7t il product namsa7 il taswira 
    product=models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name="name of product ")
    proImag=models.ImageField(upload_to="proImages/%y/%m/%d",verbose_name="image")
    
    def __str__(self):
        return str(self.product)
  
    
class Product_Alternative(models.Model):
    class Meta:
        verbose_name= ("product alternatives")
        verbose_name_plural= ("product alternatives")
    PlanProduct=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="main_product")
    PlanALTERNATIVES=models.ManyToManyField(Product,related_name="alternative_product")


class Product_Accessoires(models.Model):
    class Meta:
        verbose_name= ("product accessoires")
        verbose_name_plural= ("product accessoires")
    AccProduct=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="accessoires_product")
    PlanAcc=models.ManyToManyField(Product,related_name="accessoires_product_plan")
