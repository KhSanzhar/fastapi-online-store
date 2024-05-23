from rest_framework import viewsets
from django.shortcuts import render
from .models import Category, Product, Customer, Order, OrderItem, Review
from .serializers import CategorySerializer, ProductSerializer, CustomerSerializer, OrderSerializer, OrderItemSerializer, ReviewSerializer

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
