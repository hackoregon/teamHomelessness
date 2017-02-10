from rest_framework import serializers
from . import models


class DisabilitySerializer(serializers.ModelSerializer):
    class Meta: 
        model = models.Disability
        fields = '__all__'

class EthnicitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ethnicity
        fields = '__all__'

class GenderSerializer(serializers.ModelSerializer):
    class Meta: 
        model = models.Gender
        fields = '__all__'

class GeographiclocationSerializer(serializers.ModelSerializer):
    class Meta: 
        model = models.Geographiclocation
        fields = '__all__'

class HomelessindividualsSerializer(serializers.ModelSerializer):
    class Meta: 
        model = models.Homelessindividuals
        fields = '__all__'

class VeteransSerializer(serializers.ModelSerializer):
    class Meta: 
        model = models.Veterans
        fields = '__all__'
