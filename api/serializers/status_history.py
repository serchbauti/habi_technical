from rest_framework import serializers
from api.models import StatusHistory
from api.serializers.property import PropertySerializer
from api.serializers.status import Status
from api.serializers.status import StatusSerializer


class StatusHistorySerializer(serializers.ModelSerializer):
    status = StatusSerializer()
    property = PropertySerializer()

    class Meta:
        model = StatusHistory
        fields = "__all__"

