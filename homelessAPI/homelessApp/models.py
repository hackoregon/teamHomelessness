from django.db import models
from django.contrib.postgres.fields import IntegerRangeField


class BaseModel(models.Model):
    count = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    page = models.IntegerField(blank=True, null=True)
    
    class Meta:
        abstract = True


class AgeHouseComposition(BaseModel):
    age = IntegerRangeField(null=True)
    householdtype = models.CharField(max_length=255)
    sheltertype = models.CharField(max_length=255)

    class Meta:
        db_table = 'agehousecomposition'


class Disability(BaseModel):
    disabilitytype = models.CharField(max_length=255, blank=True, null=True)
    sheltertype = models.CharField(max_length=255)

    class Meta:
        db_table = 'disability'


class Ethnicity(BaseModel):
    ethnicity = models.CharField(max_length=255, blank=True, null=True)
    sheltertype = models.CharField(max_length=255)

    class Meta:
        db_table = 'ethnicity'


class Gender(BaseModel):
    gender = models.CharField(max_length=255)
    agerange = models.CharField(max_length=255, blank=True, null=True)
    sheltertype = models.CharField(max_length=255)

    class Meta:
        db_table = 'gender'


class GeographicLocation(BaseModel):
    geographiclocation = models.CharField(max_length=255)

    class Meta:
        db_table = 'geographiclocation'


class HomelessIndividuals(BaseModel):
    sheltertype = models.CharField(max_length=255)
    age = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'homelessindividuals'


class Veterans(BaseModel):
    veteran = models.CharField(max_length=255, blank=True, null=True)
    sheltertype = models.CharField(max_length=255)

    class Meta:
        db_table = 'veterans'


class ChronicHomelessness(BaseModel):
    chronichomelessnesstype = models.CharField(max_length=255)
    sheltertype = models.CharField(max_length=255)

    class Meta: 
        db_table = 'chronichomelessness'


class DomesticViolence(BaseModel):
    sheltertype = models.CharField(max_length=255)

    class Meta: 
        db_table = 'domesticviolence'


class SleepingLocation(BaseModel):
    sleepinglocation = models.CharField(max_length=255)

    class Meta: 
        db_table = 'sleepinglocation'


class LengthOfHomelessness(BaseModel):
    lengthofhomelessnesstype = models.CharField(max_length=255)

    class Meta:
        db_table = 'lengthofhomelessness'









