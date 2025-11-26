from rest_framework import serializers
from .models import ProductModel, CategoryModel, TypeModel


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ('id', 'sort', 'cost', 'info', 'category')
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ('id', 'name', 'info')
class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeModel
        fields = ('id', 'name', 'info')

