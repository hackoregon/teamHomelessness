from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse

from . import serializers
from . import models

class BaseListView(generics.ListAPIView):
    """
    abstract class that adds query string year search to all
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
    """
    Returns disability data from 2007 - 2015 PIT reports on odd years 

    Optionally to filter by year pass in a query string parameter called 'year'

    Ex. /disability/?year=2015 --> will return results only from 2015  
    """
    queryset = models.Disability.objects
    serializer_class = serializers.DisabilitySerializer


class ListEthnicity(BaseListView):
    """
    Returns ethnicity data from 2007 - 2015 PIT reports on odd years 

    Optionally to filter by year pass in a query string parameter called 'year'

    Ex. /ethnicity/?year=2015 --> will return results only from 2015  
    """
    queryset = models.Ethnicity.objects.all()
    serializer_class = serializers.EthnicitySerializer


class ListGender(BaseListView):
    """
    Returns gender data from 2007 - 2015 PIT reports on odd years 

    Optionally to filter by year pass in a query string parameter called 'year'

    Ex. /gender/?year=2015 --> will return results only from 2015  
    """
    queryset = models.Gender.objects.all()
    serializer_class = serializers.GenderSerializer


class ListGeographiclocation(BaseListView):
    """
    Returns geographic data from 2007 - 2015 PIT reports on odd years 

    Optionally to filter by year pass in a query string parameter called 'year'

    Ex. /geolocation/?year=2015 --> will return results only from 2015  
    """
    queryset = models.GeographicLocation.objects.all()
    serializer_class = serializers.GeographicLocationSerializer


class ListHomelessindividuals(BaseListView):
    """
    Returns data about adults vs. children in specific types of shelters from 2007 - 2015 PIT reports on odd years 

    Optionally to filter by year pass in a query string parameter called 'year'

    Ex. /individuals/?year=2015 --> will return results only from 2015  
    """
    queryset = models.HomelessIndividuals.objects.all()
    serializer_class = serializers.HomelessIndividualsSerializer


class ListVeterans(BaseListView):
    """
    Returns data about veterans from 2007 - 2015 PIT reports on odd years 

    Optionally to filter by year pass in a query string parameter called 'year'

    Ex. /veterans/?year=2015 --> will return results only from 2015  
    """
    queryset = models.Veterans.objects.all()
    serializer_class = serializers.VeteransSerializer


class ListAgeHouseComp(BaseListView):
    """
    Returns data about the age house composition from 2007 - 2015 PIT reports on odd years 

    Optionally to filter by year pass in a query string parameter called 'year'

    Ex. /agehousecomp/?year=2015 --> will return results only from 2015  
    """
    queryset = models.AgeHouseComposition.objects.all()
    serializer_class = serializers.AgeHouseCompositionSerializer


class ListChronicHomelessness(BaseListView):
    """
    Returns data chronic homelessness from 2007 - 2015 PIT reports on odd years 

    Optionally to filter by year pass in a query string parameter called 'year'

    Ex. /chronic/?year=2015 --> will return results only from 2015  
    """
    queryset = models.ChronicHomelessness.objects.all()
    serializer_class = serializers.ChronicHomelessnessSerializer


class ListDomesticViolence(BaseListView):
    """
    Returns data about domestic violence from 2007 - 2015 PIT reports on odd years 

    Optionally to filter by year pass in a query string parameter called 'year'

    Ex. /domesticviolence/?year=2015 --> will return results only from 2015  
    """
    queryset = models.DomesticViolence.objects.all()
    serializer_class = serializers.DomesticViolenceSerializer


class ListLengthOfHomelessness(BaseListView):
    """
    Returns data about the length of time people have been homeless from 2007 - 2015 PIT reports on odd years 

    Optionally to filter by year pass in a query string parameter called 'year'

    Ex. /length/?year=2015 --> will return results only from 2015  
    """
    queryset = models.LengthOfHomelessness.objects.all()
    serializer_class = serializers.LengthOfHomelessnessSerializer


class ListSleepingLocation(BaseListView):
    """
    Returns data about the sleeping locations of the homeless from 2007 - 2015 PIT reports on odd years 

    Optionally to filter by year pass in a query string parameter called 'year'

    Ex. /sleeping/?year=2015 --> will return results only from 2015  
    """
    queryset = models.SleepingLocation.objects.all()
    serializer_class = serializers.SleepingLocationSerializer

# -------------------------------------------------------------------
# acs views

class ListPitacscomp(generics.ListAPIView):
    """
    Returns percentage differences between the homeless and general Multnomah population for age and gender
    """
    queryset = models.Pitacscomp.objects.all()
    serializer_class = serializers.PitacscompSerializer


class ListPitacsethcomp(generics.ListAPIView):
    """
    Returns the percentage breakdowns of ethnicity from the homeless, those living in poverty, and general Multnomah county populations  
    """
    queryset = models.Pitacsethcomp.objects.all()
    serializer_class = serializers.PitacsethcompSerializer


class ListAcsage(generics.ListAPIView):
    queryset = models.Acsage.objects.all()
    serializer_class = serializers.AcsageSerializer

class ListAcsdisability(generics.ListAPIView):
    queryset = models.Acsdisability.objects.all()
    serializer_class = serializers.AcsdisabilitySerializer

class ListAcsrace(generics.ListAPIView):
    queryset = models.Acsrace.objects.all()
    serializer_class = serializers.AcsraceSerializer

class ListAcsveteran(generics.ListAPIView):
    queryset = models.Acsveteran.objects.all()
    serializer_class = serializers.AcsveteranSerializer

# -------------------------------------------------------------------
# 211 views

class ListBinnedAge211(generics.ListAPIView):
    """
    Returns 211 data with the age breakdown of people using the service
    """
    queryset = models.BinnedAge211.objects.all()
    serializer_class = serializers.BinnedAge211Serializer


class ListGender211(generics.ListAPIView):
    """
    Returns 211 data with the gender breakdown of people using the service
    """
    queryset = models.Gender211.objects.all()
    serializer_class = serializers.Gender211Serializer


class ListMilitary211(generics.ListAPIView):
    """
    Returns 211 data with the military status of those using the service
    """
    queryset = models.Military211.objects.all()
    serializer_class = serializers.Military211Serializer


class ListMonthDemand211(generics.ListAPIView):
    """
    Returns the counts of how many times 211 was used by month
    """
    queryset = models.MonthDemand211.objects.all()
    serializer_class = serializers.MonthDemand211Serializer


class ListService211(generics.ListAPIView):
    """
    Returns information about the types of services 211 provided
    """
    queryset = models.Service211.objects.all()
    serializer_class = serializers.Service211Serializer