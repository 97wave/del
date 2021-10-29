# TODO: опишите сериализаторы

from rest_framework import serializers
from measurements.models import Measurement, Project

class ProjectModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class MeasurementModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = "__all__"