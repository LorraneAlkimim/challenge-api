from rest_framework import serializers
from .models import Customer, Seller


class CustomerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Customer
    fields = '__all__'

class SellerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Seller
    fields = '__all__'