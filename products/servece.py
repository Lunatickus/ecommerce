from django_filters import rest_framework as filters
from .models import Product


class CharFilterInFilters(filters.BaseInFilter, filters.CharFilter):
    pass


class ProductFilter(filters.FilterSet):
    # categorys = CharFilterInFilters(field_name='category__category_name', lookup_expr='in')
    categorys = filters.CharFilter(field_name='category__category_name')
    price = filters.RangeFilter()

    class Meta:
        model = Product
        fields = ['category', 'price']
