from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.products.serializers import ProductSerializer, CategorySerializer, TypeSerializer
from .models import ProductModel, CategoryModel, TypeModel


# Create your views here.
class ProductListAPIView(ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = ProductModel.objects.all()

class ProductDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = ProductModel.objects.all()

class CategoryListAPIView(ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = CategoryModel.objects.all()

class CategoryDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = CategoryModel.objects.all()

class TypeListAPIView(ListCreateAPIView):
    serializer_class = TypeSerializer
    queryset = TypeModel.objects.all()

class TypeDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TypeSerializer
    queryset = TypeModel.objects.all()
