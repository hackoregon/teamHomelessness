from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse

from . import serializers
from . import models

class BaseListView(generics.ListAPIView):
    """
    abstract class that adds querystring year search to all
    generics.ListAPIView views using querystring params.

    Ex.
    http://example.com/homeless/<endpoint_name>/?year=2015
    """

    def get_queryset(self):
        queryset = self.queryset.all()
        year_url = self.request.query_params.get('year', None)

        if year_url is not None:
            queryset = queryset.filter(year__exact=year_url)
        return queryset

    class Meta:
        abstract = True

class ListDisability(BaseListView):
    """Add documentation for endpoint use here"""
    queryset = models.Disability.objects
    serializer_class = serializers.DisabilitySerializer


class ListEthnicity(BaseListView):
    """Add documentation for endpoint use here"""
    queryset = models.Ethnicity.objects.all()
    serializer_class = serializers.EthnicitySerializer


class ListGender(BaseListView):
    queryset = models.Gender.objects.all()
    serializer_class = serializers.GenderSerializer


class ListGeographiclocation(BaseListView):
    queryset = models.GeographicLocation.objects.all()
    serializer_class = serializers.GeographicLocationSerializer


class ListHomelessindividuals(BaseListView):
    queryset = models.HomelessIndividuals.objects.all()
    serializer_class = serializers.HomelessIndividualsSerializer


class ListVeterans(BaseListView):
    queryset = models.Veterans.objects.all()
    serializer_class = serializers.VeteransSerializer


class ListAgeHouseComp(BaseListView):
    queryset = models.AgeHouseComposition.objects.all()
    serializer_class = serializers.AgeHouseCompositionSerializer


class ListChronicHomelessness(BaseListView):
    queryset = models.ChronicHomelessness.objects.all()
    serializer_class = serializers.ChronicHomelessnessSerializer


class ListDomesticViolence(BaseListView):
    queryset = models.DomesticViolence.objects.all()
    serializer_class = serializers.DomesticViolenceSerializer


class ListLengthOfHomelessness(BaseListView):
    queryset = models.LengthOfHomelessness.objects.all()
    serializer_class = serializers.LengthOfHomelessnessSerializer


class ListSleepingLocation(BaseListView):
    queryset = models.SleepingLocation.objects.all()
    serializer_class = serializers.SleepingLocationSerializer

class ListAcsage(BaseListView):
    queryset = models.Acsage.objects.all()
    serializer_class = serializers.AcsageSerializer

class ListAcsdisability(BaseListView):
    queryset = models.Acsdisability.objects.all()
    serializer_class = serializers.AcsdisabilitySerializer

class ListAcsrace(BaseListView):
    queryset = models.Acsrace.objects.all()
    serializer_class = serializers.AcsraceSerializer

class ListAcsveteran(BaseListView):
    queryset = models.Acsveteran.objects.all()
    serializer_class = serializers.AcsveteranSerializer
