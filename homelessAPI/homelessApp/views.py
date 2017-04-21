from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse

from . import serializers
from . import models
from . import filters


class ListDisability(generics.ListAPIView):
    """
    Returns disability data from 2007 - 2015 PIT reports on odd years 

    Optionally to filter by year pass in a query string parameter called 'year'

    Ex. /disability/?year=2015 --> will return results only from 2015  
    """
    queryset = models.Disability.objects
    serializer_class = serializers.DisabilitySerializer
    filter_class = filters.DisabilityFilter


class ListEthnicity(generics.ListAPIView):
    """
    Returns ethnicity data from 2007 - 2015 PIT reports on odd years 

    Optionally to filter by year pass in a query string parameter called 'year'

    Ex. /ethnicity/?year=2015 --> will return results only from 2015  
    """
    queryset = models.Ethnicity.objects.all()
    serializer_class = serializers.EthnicitySerializer
    filter_class = filters.EthnicityFilter


class ListGender(generics.ListAPIView):
    """
    Returns gender data from 2007 - 2015 PIT reports on odd years 

    Optionally to filter by year pass in a query string parameter called 'year'

    Ex. /gender/?year=2015 --> will return results only from 2015  
    """
    queryset = models.Gender.objects.all()
    serializer_class = serializers.GenderSerializer
    filter_class = filters.GenderFilter


class ListGeographiclocation(generics.ListAPIView):
    """
    Returns geographic data from 2007 - 2015 PIT reports on odd years 

    Optionally to filter by year pass in a query string parameter called 'year'

    Ex. /geolocation/?year=2015 --> will return results only from 2015  
    """
    queryset = models.GeographicLocation.objects.all()
    serializer_class = serializers.GeographicLocationSerializer
    filter_class = filters.GeographicLocationFilter


class ListHomelessindividuals(generics.ListAPIView):
    """
    Returns data about adults vs. children in specific types of shelters from 2007 - 2015 PIT reports on odd years 

    Optionally to filter by year pass in a query string parameter called 'year'

    Ex. /individuals/?year=2015 --> will return results only from 2015  
    """
    queryset = models.HomelessIndividuals.objects.all()
    serializer_class = serializers.HomelessIndividualsSerializer
    filter_class = filters.HomelessIndividualsFilter


class ListVeterans(generics.ListAPIView):
    """
    Returns data about veterans from 2007 - 2015 PIT reports on odd years 

    Optionally to filter by year pass in a query string parameter called 'year'

    Ex. /veterans/?year=2015 --> will return results only from 2015  
    """
    queryset = models.Veterans.objects.all()
    serializer_class = serializers.VeteransSerializer
    filter_class = filters.VeteransFilter


class ListAgeHouseComp(generics.ListAPIView):
    """
    Returns data about the age house composition from 2007 - 2015 PIT reports on odd years 

    Optionally to filter by year pass in a query string parameter called 'year'

    Ex. /agehousecomp/?year=2015 --> will return results only from 2015  
    """
    queryset = models.AgeHouseComposition.objects.all()
    serializer_class = serializers.AgeHouseCompositionSerializer
    filter_class = filters.AgeHouseCompositionFilter


class ListChronicHomelessness(generics.ListAPIView):
    """
    Returns data chronic homelessness from 2007 - 2015 PIT reports on odd years 

    Optionally to filter by year pass in a query string parameter called 'year'

    Ex. /chronic/?year=2015 --> will return results only from 2015  
    """
    queryset = models.ChronicHomelessness.objects.all()
    serializer_class = serializers.ChronicHomelessnessSerializer
    filter_class = filters.ChronicHomelessnessFilter


class ListDomesticViolence(generics.ListAPIView):
    """
    Returns data about domestic violence from 2007 - 2015 PIT reports on odd years 

    Optionally to filter by year pass in a query string parameter called 'year'

    Ex. /domesticviolence/?year=2015 --> will return results only from 2015  
    """
    queryset = models.DomesticViolence.objects.all()
    serializer_class = serializers.DomesticViolenceSerializer
    filter_class = filters.DomesticViolenceFilter


class ListLengthOfHomelessness(generics.ListAPIView):
    """
    Returns data about the length of time people have been homeless from 2007 - 2015 PIT reports on odd years 

    Optionally to filter by year pass in a query string parameter called 'year'

    Ex. /length/?year=2015 --> will return results only from 2015  
    """
    queryset = models.LengthOfHomelessness.objects.all()
    serializer_class = serializers.LengthOfHomelessnessSerializer
    filter_class = filters.LengthOfHomelessnessFilter


class ListSleepingLocation(generics.ListAPIView):
    """
    Returns data about the sleeping locations of the homeless from 2007 - 2015 PIT reports on odd years 

    Optionally to filter by year pass in a query string parameter called 'year'

    Ex. /sleeping/?year=2015 --> will return results only from 2015  
    """
    queryset = models.SleepingLocation.objects.all()
    serializer_class = serializers.SleepingLocationSerializer
    filter_class = filters.SleepingLocationFilter

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