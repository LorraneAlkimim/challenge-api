from django.contrib import admin
from .models import Customer, Seller, Product, CommissionPercentageByWeekday

admin.site.register(Customer)
admin.site.register(Seller)
admin.site.register(Product)
admin.site.register(CommissionPercentageByWeekday)