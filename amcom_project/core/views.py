from rest_framework import viewsets
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CustomerSerializer, SellerSerializer, ProductSerializer, SaleSerializer, SaleCreateSerializer, SaleUpdateSerializer
from .models import Customer, Seller, Product, Sale


class CustomerViewset(viewsets.ModelViewSet):
  queryset = Customer.objects.all()
  serializer_class = CustomerSerializer

class SellerViewset(viewsets.ModelViewSet):
  queryset = Seller.objects.all()
  serializer_class = SellerSerializer

class ProductViewset(viewsets.ModelViewSet):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer

class SaleViewset(viewsets.ModelViewSet):
  queryset = Sale.objects.all()
  serializer_class = SaleSerializer
  http_method_names = ['get', 'delete']

class SaleCreateViewset(APIView):
  def post(self, request):
    serializer = SaleCreateSerializer(data=request.data)
    
    if serializer.is_valid():
      sale = serializer.save()

      return Response({'id': sale.invoice_code}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SaleUpdateViewset(APIView):
  def put(self, request, invoice_code):
    try:
      sale = Sale.objects.get(invoice_code=invoice_code)
    except Sale.DoesNotExist:
      return Response({"detail": "Sale not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = SaleUpdateSerializer(sale, data=request.data)
    if serializer.is_valid():
      products = request.data.get('products', None)
      if products is not None:
        sale.products.clear()

        for product_data in products:
          product_id = product_data['id']
          quantity = product_data['quantity']
          sale.products.add(product_id, through_defaults={'quantity': quantity})
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def patch(self, request, invoice_code):
    try:
        sale = Sale.objects.get(invoice_code=invoice_code)
    except Sale.DoesNotExist:
      return Response({"detail": "Sale not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = SaleUpdateSerializer(sale, data=request.data, partial=True)
    if serializer.is_valid():
      products = request.data.get('products', None)
      if products is not None:
          for product_data in products:
              product_id = product_data['id']
              quantity = product_data['quantity']
              
              sale.products.update_or_create(product_id, defaults={'quantity': quantity})
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)