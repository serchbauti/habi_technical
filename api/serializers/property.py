from rest_framework import serializers
from api.models import Property
from api.models import StatusHistory
from django.db.models import OuterRef, Subquery
from django.db.models import Q


class PropertySerializer(serializers.ModelSerializer):

    status = serializers.SerializerMethodField()

    class Meta:
        model = Property
        fields = "__all__"

    def get_status(self, obj):
        status = StatusHistory.objects.filter(
            property=obj).filter(
            (
                Q(status__name="pre_venta")
                | Q(status__name="en_venta")
                | Q(status__name="vendido")
            )).last()
        if getattr(status, 'status', None):
            return status.status.name
