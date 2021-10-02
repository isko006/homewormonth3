from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductListSerialiser
from .models import Product

# Create your views here.

@api_view(['GET'])
def movies_list_view(request):
    product = Product.objects.all()
    data =  ProductListSerialiser(product, many=True).data
    return Response(data=data)



@api_view(['GET'])
def movies_item_view(request, pk):
    try:
        products = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        return Response(data={'message': "Product not Found"}, status=status.HTTP_404_NOT_FOUND)

    data = ProductListSerialiser(products).data
    return Response(data=data)