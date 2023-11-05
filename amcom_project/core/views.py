from rest_framework import viewsets
from .serializers import CustomerSerializer, SellerSerializer, ProductSerializer
from .models import Customer, Seller, Product


class CustomerViewset(viewsets.ModelViewSet):
  queryset = Customer.objects.all()
  serializer_class = CustomerSerializer

class SellerViewset(viewsets.ModelViewSet):
  queryset = Seller.objects.all()
  serializer_class = SellerSerializer

class ProductViewset(viewsets.ModelViewSet):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer