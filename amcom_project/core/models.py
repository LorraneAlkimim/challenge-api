import uuid
from django.db import models
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