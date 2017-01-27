from rest_framework import serializers
from . import models


class EthnicitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ethnicity
        fields = '__all__'
