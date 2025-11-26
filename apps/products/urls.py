from django.urls import path

from apps.products.views import ProductListAPIView, ProductDetailAPIView, CategoryDetailAPIView, CategoryListAPIView, TypeDetailAPIView, TypeListAPIView

urlpatterns = [
    path('', ProductListAPIView.as_view()),
    path('<int:pk>/', ProductDetailAPIView.as_view()),
    path('category/', CategoryListAPIView.as_view()),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view()),
    path('type/', TypeListAPIView.as_view()),
    path('type/<int:pk>/', TypeDetailAPIView.as_view()),
]