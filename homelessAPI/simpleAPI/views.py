from rest_framework import generics
from .serializers import EthnicitySerializer
from .models import Ethnicity


class ListEthnicity(generics.ListAPIView):
    queryset = Ethnicity.objects.all()
    serializer_class = EthnicitySerializer
