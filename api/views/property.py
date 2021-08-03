from rest_framework.viewsets import ModelViewSet
from api.serializers.property import PropertySerializer
from api.serializers.status_history import StatusHistorySerializer
from api.models import Property
from api.models import StatusHistory
from django.db.models import OuterRef, Subquery
from django.db.models import Prefetch
from django.db.models import Q
from django_filters import rest_framework as filters
from api.filters import PropertyFilter


class PropertyView(ModelViewSet):
    serializer_class = PropertySerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = PropertyFilter

    def get_queryset(self):
        return Property.objects.exclude(statushistory__status__name__isnull=True)
