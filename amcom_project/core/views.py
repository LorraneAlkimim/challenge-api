from rest_framework import viewsets
from .serializers import CustomerSerializer, SellerSerializer
from .models import Customer, Seller


class CustomerViewset(viewsets.ModelViewSet):
  queryset = Customer.objects.all()
  serializer_class = CustomerSerializer

class SellerViewset(viewsets.ModelViewSet):
  queryset = Seller.objects.all()
  serializer_class = SellerSerializer