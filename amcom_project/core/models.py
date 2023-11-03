import uuid
from django.db import models
from datetime import datetime
from django.db.models import DateTimeField
from phonenumber_field.modelfields import PhoneNumberField


class Person(models.Model):
  name = models.CharField(max_length = 100)
  email = models.EmailField()
  phone = PhoneNumberField(null=False, blank=False, unique=True)

  def __str__(self):
    return self.name

  class Meta:
    abstract = True


class Customer(Person):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


class Seller(Person):
  seller_code = models.AutoField(primary_key=True)


class Product(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  code = models.CharField(max_length = 50)
  description = models.CharField(max_length = 100)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  commission_percentage = models.DecimalField(max_digits=4, decimal_places=2)

  def __str__(self):
    return self.description


class Sale(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  invoice_code = models.CharField(max_length = 50)
  date = models.DateTimeField(default=datetime.now, blank=True)
  customer = models.ForeignKey(Customer, on_delete=models.RESTRICT)
  seller = models.ForeignKey(Seller, on_delete=models.RESTRICT)
  products = models.ManyToManyField(Product, through='SaleProduct')

  def calculate_sale_total_value(self):
    total_value = sum(product.calculate_total_price() for product in self.saleproduct_set.all())
    return total_value
  
  def calculate_total_commission(self):
    total_commission = sum(product.calculate_product_commission() for product in self.saleproduct_set.all())
    return total_commission
  
  def count_items(self):
    quantity_of_items = sum(product.quantity for product in self.saleproduct_set.all())
    return quantity_of_items


class SaleProduct(models.Model):
  product = models.ForeignKey('Product', on_delete=models.CASCADE)
  sale = models.ForeignKey('Sale', on_delete=models.CASCADE)
  quantity = models.IntegerField(default=1)

  def calculate_total_price(self):
    return self.product.price * self.quantity
  
  def calculate_product_commission(self):
    product_total_price = self.calculate_total_price()
    product_commission = (self.product.commission_percentage/100) * product_total_price
    return round(product_commission, 2)

  class Meta:
    constraints = [
      models.UniqueConstraint(fields=('product', 'sale'), name='once_per_sale_product')
    ]