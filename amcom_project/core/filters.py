import django_filters

from .models import Person, Product

class PersonFilter(django_filters.FilterSet):
  name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')

  class Meta:
    model = Person
    fields = ['name']

class ProductFilter(django_filters.FilterSet):
  code = django_filters.CharFilter(field_name='code', lookup_expr='icontains')
  description = django_filters.CharFilter(field_name='description', lookup_expr='icontains')

  class Meta:
    model = Product
    fields = ['code', 'description']