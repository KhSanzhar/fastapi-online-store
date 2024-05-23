from rest_framework import viewsets
from django.shortcuts import render
from .models import Category, Product, Customer, Order, OrderItem, Review
from .serializers import CategorySerializer, ProductSerializer, CustomerSerializer, OrderSerializer, OrderItemSerializer, ReviewSerializer

from rest_framework.decorators import api_view, schema
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/products.html', {'products': products})


@swagger_auto_schema(
    method='get',
    manual_parameters=[
        openapi.Parameter('category', openapi.IN_QUERY, description="Category ID", type=openapi.TYPE_INTEGER)
    ],
    responses={200: openapi.Response('A list of products', ProductSerializer(many=True))}
)
@api_view(['GET'])
def product_list(request):
    category_id = request.GET.get('category')
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


# @swagger_auto_schema(
#     method='get',
#     operation_description="Retrieve a list of products",
#     responses={200: openapi.Response('A list of products', ProductSerializer(many=True))}
# )
#
# @api_view(['GET'])
# def product_list(request):
#     products = Product.objects.all()
#     serializer = ProductSerializer(products, many=True)
#     return Response(serializer.data)