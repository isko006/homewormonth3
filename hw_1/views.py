from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductListSerializer, ProductsActiveTagsListSerializer, CategoryListSerializer, ProductsReviewListSerializer
from .models import Product, Category

# Create your views here.

@api_view(['GET'])
def movies_list_view(request):
    product = Product.objects.all()
    data =  ProductListSerializer(product, many=True).data
    return Response(data=data)



@api_view(['GET'])
def movies_item_view(request, pk):
    try:
        products = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        return Response(data={'message': "Product not Found"}, status=status.HTTP_404_NOT_FOUND)

    data = ProductListSerializer(products).data
    return Response(data=data)


@api_view(['GET'])
def reviews_list_view(request):
    products = Product.objects.all()
    data = ProductsReviewListSerializer(products, many=True).data
    return Response(data=data)


@api_view(['GET'])
def active_tags_list_view(request):
    products = Product.objects.all()
    data = ProductsActiveTagsListSerializer(products, many=True).data
    return Response(data=data)




@api_view(['GET'])
def categories_list_view(request):
    category = Category.objects.all()
    data = CategoryListSerializer(category).data

    return data
























