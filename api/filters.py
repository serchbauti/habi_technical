import django_filters
from api.models import Property

class PropertyFilter(django_filters.FilterSet):
    city = django_filters.CharFilter(field_name='city', lookup_expr='exact')
    year = django_filters.NumberFilter(field_name='year', lookup_expr='exact')
    status = django_filters.CharFilter(
        field_name='statushistory__status__name', lookup_expr='iexact'
    )

    class Meta:
        model = Property
        fields = ('city', 'year', 'status')
