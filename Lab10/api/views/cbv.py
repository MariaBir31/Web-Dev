from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import Product
from api.serializers import Product2Serializer


class ProductListAPIView(APIView):

    def get(self, request):
        products = Product.objects.all()
        return Response(Product2Serializer(products, many=True).data)

    def post(self, request):
        serializer = Product2Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors)


class ProductDetailAPIView(APIView):

    def get_object(self, product_id):
        try:
            return Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            return None

    def get(self, request, product_id):
        product = self.get_object(product_id)
        if not product:
            return Response({'error': 'Not found'}, status=404)
        return Response(Product2Serializer(product).data)

    def put(self, request, product_id):
        product = self.get_object(product_id)
        serializer = Product2Serializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, product_id):
        product = self.get_object(product_id)
        product.delete()
        return Response({'message': 'Deleted'})