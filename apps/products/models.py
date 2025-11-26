from django.db import models

# Create your models here.
from core.models import BaseModel

class TypeModel(BaseModel):
    class Meta:
        db_table = 'type'
    name = models.CharField(max_length=50, unique=True)
    info = models.TextField(blank=True, null=True)

class CategoryModel(BaseModel):
    class Meta:
        db_table = 'category'
    name = models.CharField(max_length=50, unique=True)
    info = models.TextField(blank=True, null=True)
    type = models.ForeignKey(TypeModel, on_delete=models.CASCADE, related_name='categories')

class ProductModel(BaseModel):
    class Meta:
        db_table = 'product'
    sort = models.CharField(max_length=50)
    cost = models.IntegerField()
    info = models.TextField(blank=True, null=True)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name='products')


