import uuid
from django.db import models
from datetime import datetime
from django.db.models import DateTimeField
from phonenumber_field.modelfields import PhoneNumberField


class Person(models.Model):
  name = models.CharField(max_length = 100, null=False, blank=False, unique=True)
  email = models.EmailField(null=False, blank=False, unique=True)
  phone = PhoneNumberField(null=False, blank=False, unique=True)

  class Meta:
    abstract = True

  def __str__(self):
    return self.name


class Customer(Person):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

  class Meta:
    ordering = ['name']
    db_table = 'customer'


class Seller(Person):
  seller_code = models.AutoField(primary_key=True, editable=False)

  class Meta:
    ordering = ['seller_code', 'name']
    db_table = 'seller'


class CommissionPercentageByWeekday(models.Model):
  WEEKDAYS = (
    (0, 'Monday'),
    (1, 'Tuesday'),
    (2, 'Wednesday'),
    (3, 'Thursday'),
    (4, 'Friday'),
    (5, 'Saturday'),
    (6, 'Sunday'),
  )

  weekday = models.PositiveIntegerField(choices=WEEKDAYS, unique=True, null=False, blank=False)
  minimum_percentage = models.DecimalField(max_digits=4, decimal_places=2, null=False, blank=False)
  maximum_percentage = models.DecimalField(max_digits=4, decimal_places=2, null=False, blank=False)

  class Meta:
    db_table = 'commission_percentage_by_weekday'

  def __str__(self):
    return self.get_weekday_display()


class Product(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  code = models.CharField(max_length = 50, null=False, blank=False, unique=True)
  description = models.CharField(max_length = 100, null=False, blank=False)
  price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
  commission_percentage = models.DecimalField(max_digits=4, decimal_places=2, null=False, blank=False)

  class Meta:
    ordering = ['code', 'description']
    db_table = 'product'

  def __str__(self):
    return self.description
  
  def calculate_product_commission_percentage(self):
    """
        Calculates the applicable commission percentage based on the current day of the week.

        Returns:
        Decimal: The applicable commission percentage.

        This method checks the current day of the week and if there is a percentage
        commission associated with that day of the week, calculates the minimum
        commission or maximum if the percentage of the product is outside this
        range, or returns the product's own percentage if it is within the range.
    """

    current_weekday = datetime.today().weekday()

    try:
      percentages_by_weekday = CommissionPercentageByWeekday.objects.get(weekday=current_weekday)
      minimum_percentage = percentages_by_weekday.minimum_percentage
      maximum_percentage = percentages_by_weekday.maximum_percentage
      
      if self.commission_percentage < minimum_percentage:
        return minimum_percentage
      elif self.commission_percentage > maximum_percentage:
        return maximum_percentage
      else:
        return self.commission_percentage
    except CommissionPercentageByWeekday.DoesNotExist:
      return self.commission_percentage


class Sale(models.Model):
  invoice_code = models.AutoField(primary_key=True, editable=False)
  date = models.DateTimeField(default=datetime.now, blank=True)
  customer = models.ForeignKey(Customer, on_delete=models.RESTRICT, null=False, blank=False)
  seller = models.ForeignKey(Seller, on_delete=models.RESTRICT, null=False, blank=False,)
  products = models.ManyToManyField(Product, through='SaleProduct')

  class Meta:
    ordering = ['date', 'invoice_code']
    db_table = 'sale'

  def __str__(self):
    return f"Sale {self.invoice_code}"

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

  class Meta:
    db_table = 'sale_product'
    constraints = [
      models.UniqueConstraint(fields=('product', 'sale'), name='once_per_sale_product')
    ]

  def calculate_total_price(self):
    return self.product.price * self.quantity
  
  def calculate_product_commission(self):
    product_total_price = self.calculate_total_price()
    product_commission = (self.product.calculate_product_commission_percentage() / 100) * product_total_price
    return round(product_commission, 2)