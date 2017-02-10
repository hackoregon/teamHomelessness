from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse

from . import serializers
from . import models 


# don't need this root view if team decides to use swagger
@api_view(['GET'])
def Team_homelessness_api_root(request, format=None):
    "The following endpoints are available"
    return Response({
        'Disability table list': 
        reverse('homeless:disability-list', request=request, format=format),

        'Ethnicity table list': 
        reverse('homeless:ethnicity-list', request=request, format=format),

        'Gender table list': 
        reverse('homeless:gender-list', request=request, format=format),

        'Geographiclocation table list': 
        reverse('homeless:geo-list', request=request, format=format),

        'Homelessindividuals table list': 
        reverse('homeless:individuals-list', request=request, format=format),

        'Veterans table list': 
        reverse('homeless:veterans-list', request=request, format=format),        
    })


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
    queryset = models.Geographiclocation.objects.all()
    serializer_class = serializers.GeographiclocationSerializer

class ListHomelessindividuals(generics.ListAPIView):
    queryset = models.Homelessindividuals.objects.all()
    serializer_class = serializers.HomelessindividualsSerializer

class ListVeterans(generics.ListAPIView):
    queryset = models.Veterans.objects.all()
    serializer_class = serializers.VeteransSerializer 












