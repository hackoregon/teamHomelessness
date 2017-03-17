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


class GeographicLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GeographicLocation
        fields = '__all__'


class HomelessIndividualsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HomelessIndividuals
        fields = '__all__'


class VeteransSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Veterans
        fields = '__all__'


class AgeHouseCompositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AgeHouseComposition
        fields = '__all__'


class ChronicHomelessnessSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ChronicHomelessness
        fields = '__all__'


class DomesticViolenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DomesticViolence
        fields = '__all__'


class LengthOfHomelessnessSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LengthOfHomelessness
        fields = '__all__'


class SleepingLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SleepingLocation
        fields = '__all__'

class AcsageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Acsage
        fields = '__all__'

class AcsdisabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Acsdisability
        fields = '__all__'

class AcsraceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Acsrace
        fields = '__all__'

class AcsveteranSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Acsveteran
        fields = '__all__'
