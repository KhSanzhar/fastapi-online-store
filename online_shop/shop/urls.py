from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet, CustomerViewSet, OrderViewSet, OrderItemViewSet, ReviewViewSet, product_list

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order-items', OrderItemViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('products/', product_list, name='product-list'),
]
