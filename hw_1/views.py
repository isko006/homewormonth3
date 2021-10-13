from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductListSerializer, ProductsActiveTagsListSerializer, CategoryListSerializer, ProductsReviewListSerializer, ProductCreateValidateSerializer
from .models import Product, Category

# Create your views here.

@api_view(['GET', 'POST',])
def movies_list_view(request):
    if request.method == 'POST':
        serializer = ProductCreateValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                data={'massage': 'error',
                      'errors': serializer.errors},
                status=status.HTTP_406_NOT_ACCEPTABLE
            )

        title = request.data.get('title', '')
        description = request.data.get('description', '')
        price = request.data.get('price', 0)
        product = Product.objects.create(title=title, description=description, price=price, )
        product.save()
        return Response(data={'massage': 'you created movie!',
                              'movie': ProductListSerializer(product).data})

    product = Product.objects.all()
    data = ProductListSerializer(product, many=True).data
    return Response(data=data)



@api_view(['GET', 'PUT', 'DELETE'])
def movies_item_view(request, pk):
    try:
        products = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        return Response(data={'message': "Product not Found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        products.delete()
        return Response(data={'massage': 'Product removed!!!'})
    elif request.method == 'PUT':
        serializer = ProductCreateValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                data={'massage': 'error',
                      'errors': serializer.errors},
                status=status.HTTP_406_NOT_ACCEPTABLE
            )
        products.title = request.data.get('title')
        products.description = request.data.get('description')
        products.price = request.data.get('price')
        products.save()
        return Response(data={'massage': 'Product updated',
                              'products': ProductListSerializer(Product).data})
    data = ProductListSerializer(products, many=False).data
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
























