from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse

from . import serializers
from . import models 


class ListDisability(generics.ListAPIView):
    """Add documentation for endpoint use here"""
    queryset = models.Disability.objects.all()
    serializer_class = serializers.DisabilitySerializer


class ListEthnicity(generics.ListAPIView):
    """Add documentation for endpoint use here"""
    queryset = models.Ethnicity.objects.all()
    serializer_class = serializers.EthnicitySerializer


class ListGender(generics.ListAPIView):
    queryset = models.Gender.objects.all()
    serializer_class = serializers.GenderSerializer


class ListGeographiclocation(generics.ListAPIView):
    queryset = models.GeographicLocation.objects.all()
    serializer_class = serializers.GeographicLocationSerializer


class ListHomelessindividuals(generics.ListAPIView):
    queryset = models.HomelessIndividuals.objects.all()
    serializer_class = serializers.HomelessIndividualsSerializer


class ListVeterans(generics.ListAPIView):
    queryset = models.Veterans.objects.all()
    serializer_class = serializers.VeteransSerializer 


class ListAgeHouseComp(generics.ListAPIView):
    queryset = models.AgeHouseComposition.objects.all()
    serializer_class = serializers.AgeHouseCompositionSerializer


class ListChronicHomelessness(generics.ListAPIView):
    queryset = models.ChronicHomelessness.objects.all()
    serializer_class = serializers.ChronicHomelessnessSerializer


class ListDomesticViolence(generics.ListAPIView):
    queryset = models.DomesticViolence.objects.all()
    serializer_class = serializers.DomesticViolenceSerializer


class ListLengthOfHomelessness(generics.ListAPIView):
    queryset = models.LengthOfHomelessness.objects.all()
    serializer_class = serializers.LengthOfHomelessnessSerializer


class ListSleepingLocation(generics.ListAPIView):
    queryset = models.SleepingLocation.objects.all()
    serializer_class = serializers.SleepingLocationSerializer
