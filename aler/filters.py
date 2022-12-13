import django_filters
from django_filters import RangeFilter, FilterSet
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from .models import Property

class PropertyFilter(django_filters.FilterSet):
    price = RangeFilter()
    property_type = {'property_type': ['exact']}
    contract_type = {'contract_type': ['exact']}
    state = {'state': ['exact']}
    class Meta:
        model = Property
        fields = ['contract_type', 'property_type', 'state', 'price']

class PriceFilter(FilterSet):
    price = RangeFilter()
    
    class Meta:
        model = Property
        fields = ['price']
