from django.contrib import admin
from .models import Customer, Seller, Product, Sale, SaleProduct, CommissionPercentageByWeekday

class SaleProductInline(admin.TabularInline):
  model = SaleProduct
  extra = 1

class SaleAdmin(admin.ModelAdmin):
  inlines = (SaleProductInline,)

admin.site.register(Customer)
admin.site.register(Seller)
admin.site.register(Product)
admin.site.register(Sale, SaleAdmin)
admin.site.register(CommissionPercentageByWeekday)