from django.db import models

# Create your models here.
class Brand(models.Model):
    BDName=models.CharField(max_length=40)
    BDDescription=models.TextField(blank=True,null=True)
    def __str__(self):
        return self.BDName
    

class Variant(models.Model):
    VarName=models.CharField(max_length=40)
    VarDescription=models.TextField(blank=True,null=True)
    def __str__(self):
        return self.VarName
