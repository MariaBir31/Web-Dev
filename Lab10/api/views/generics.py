from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import Product, Category
from api.serializers import Product2Serializer, CategorySerializer


class ProductListAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = Product2Serializer


class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = Product2Serializer
    lookup_url_kwarg = 'product_id'


class CategoryListAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_url_kwarg = 'category_id'


class CategoryProductsAPIView(APIView):
    def get(self, request, category_id):
        products = Product.objects.filter(category_id=category_id)
        return Response(Product2Serializer(products, many=True).data)