import django_filters

from . import models

class DisabilityFilter(django_filters.FilterSet):
    class Meta:
        model = models.Disability
        fields = ['year',]


class EthnicityFilter(django_filters.FilterSet):
    class Meta:
        model = models.Ethnicity
        fields = ['year',]


class GenderFilter(django_filters.FilterSet):
    class Meta:
        model = models.Gender
        fields = ['year',]


class GeographicLocationFilter(django_filters.FilterSet):
    class Meta:
        model = models.GeographicLocation
        fields = ['year',]


class HomelessIndividualsFilter(django_filters.FilterSet):
    class Meta:
        model = models.HomelessIndividuals
        fields = ['year',]


class VeteransFilter(django_filters.FilterSet):
    class Meta:
        model = models.Veterans
        fields = ['year',]


class AgeHouseCompositionFilter(django_filters.FilterSet):
    class Meta:
        model = models.AgeHouseComposition
        fields = ['year',]


class ChronicHomelessnessFilter(django_filters.FilterSet):
    class Meta:
        model = models.ChronicHomelessness
        fields = ['year',]


class DomesticViolenceFilter(django_filters.FilterSet):
    class Meta:
        model = models.DomesticViolence
        fields = ['year',]


class LengthOfHomelessnessFilter(django_filters.FilterSet):
    class Meta:
        model = models.LengthOfHomelessness
        fields = ['year',]


class SleepingLocationFilter(django_filters.FilterSet):
    class Meta:
        model = models.SleepingLocation
        fields = ['year',]


# class AcsageSerializer(django_filters.FilterSet):
#     class Meta:
#         model = models.Acsage
#         fields = '__all__'


# class AcsdisabilitySerializer(django_filters.FilterSet):
#     class Meta:
#         model = models.Acsdisability
#         fields = '__all__'


# class AcsraceSerializer(django_filters.FilterSet):
#     class Meta:
#         model = models.Acsrace
#         fields = '__all__'


# class AcsveteranSerializer(django_filters.FilterSet):
#     class Meta:
#         model = models.Acsveteran
#         fields = '__all__'


# class PitacscompSerializer(django_filters.FilterSet):
#     class Meta: 
#         model = models.Pitacscomp
#         fields = '__all__'


# class PitacsethcompSerializer(django_filters.FilterSet):
#     class Meta:
#         model = models.Pitacsethcomp
#         fields = '__all__'


# class BinnedAge211Serializer(django_filters.FilterSet):
#     class Meta:
#         model = models.BinnedAge211
#         fields = '__all__'


# class Gender211Serializer(django_filters.FilterSet):
#     class Meta:
#         model = models.Gender211
#         fields = '__all__'


# class Military211Serializer(django_filters.FilterSet):
#     class Meta:
#         model = models.Military211
#         fields = '__all__'


# class MonthDemand211Serializer(django_filters.FilterSet):
#     class Meta:
#         model = models.MonthDemand211
#         fields = '__all__'


# class Service211Serializer(django_filters.FilterSet):
#     class Meta:
#         model = models.Service211
#         fields = '__all__'