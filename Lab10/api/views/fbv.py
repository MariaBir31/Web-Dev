from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from api.models import Product
from api.serializers import Product2Serializer


@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        return Response(Product2Serializer(products, many=True).data)

    elif request.method == 'POST':
        serializer = Product2Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        return Response({'error': 'Not found'}, status=404)

    if request.method == 'GET':
        return Response(Product2Serializer(product).data)

    elif request.method == 'PUT':
        serializer = Product2Serializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif request.method == 'DELETE':
        product.delete()
        return Response({'message': 'Deleted'})