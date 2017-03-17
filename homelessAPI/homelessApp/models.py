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
        verbose_name_plural = 'Age House Composition'


class Disability(BaseModel):
    disabilitytype = models.CharField(max_length=255, blank=True, null=True)
    sheltertype = models.CharField(max_length=255)

    class Meta:
        db_table = 'disability'
        verbose_name_plural = 'Disability'


class Ethnicity(BaseModel):
    ethnicity = models.CharField(max_length=255, blank=True, null=True)
    sheltertype = models.CharField(max_length=255)

    class Meta:
        db_table = 'ethnicity'
        verbose_name_plural = 'Ethnicity'


class Gender(BaseModel):
    gender = models.CharField(max_length=255)
    agerange = models.CharField(max_length=255, blank=True, null=True)
    sheltertype = models.CharField(max_length=255)

    class Meta:
        db_table = 'gender'
        verbose_name_plural = 'Gender'


class GeographicLocation(BaseModel):
    geographiclocation = models.CharField(max_length=255)

    class Meta:
        db_table = 'geographiclocation'
        verbose_name_plural = 'Geographic Location'


class HomelessIndividuals(BaseModel):
    sheltertype = models.CharField(max_length=255)
    age = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'homelessindividuals'
        verbose_name_plural = 'Homeless Individuals'


class Veterans(BaseModel):
    veteran = models.CharField(max_length=255, blank=True, null=True)
    sheltertype = models.CharField(max_length=255)

    class Meta:
        db_table = 'veterans'
        verbose_name_plural = 'Veterans'


class ChronicHomelessness(BaseModel):
    chronichomelessnesstype = models.CharField(max_length=255)
    sheltertype = models.CharField(max_length=255)

    class Meta:
        db_table = 'chronichomelessness'
        verbose_name_plural = 'Chronic Homelessness'


class DomesticViolence(BaseModel):
    sheltertype = models.CharField(max_length=255)

    class Meta:
        db_table = 'domesticviolence'
        verbose_name_plural = 'Domestic Violence'


class SleepingLocation(BaseModel):
    sleepinglocation = models.CharField(max_length=255)

    class Meta:
        db_table = 'sleepinglocation'
        verbose_name_plural = 'Sleeping Location'


class LengthOfHomelessness(BaseModel):
    lengthofhomelessnesstype = models.CharField(max_length=255)

    class Meta:
        db_table = 'lengthofhomelessness'
        verbose_name_plural = 'Length of Homelessness'

# ------------------------------------------------------------------
# ACS models

class Acsage(models.Model):
    acsid = models.CharField(max_length=1000, blank=True, null=True)
    geoid = models.CharField(max_length=255, blank=True, null=True)
#    sex = models.CharField(max_length=25, blank=True, null=True)
    age = IntegerRangeField(null=True)
    count = models.IntegerField()
    year = models.IntegerField()
    sourcefile = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'acsage'


class Acsdisability(models.Model):
    acsid = models.CharField(max_length=1000, blank=True, null=True)
    geoid = models.CharField(max_length=255, blank=True, null=True)
    disability_status = models.CharField(max_length=50, blank=True, null=True)
    count = models.IntegerField()
    year = models.IntegerField()
    sourcefile = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'acsdisability'


class Acsrace(models.Model):
    acsid = models.CharField(max_length=1000, blank=True, null=True)
    geoid = models.CharField(max_length=255, blank=True, null=True)
    race = models.CharField(max_length=50, blank=True, null=True)
    count = models.IntegerField()
    year = models.IntegerField()
    sourcefile = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'acsrace'


class Acsveteran(models.Model):
    acsid = models.CharField(max_length=1000, blank=True, null=True)
    geoid = models.CharField(max_length=255, blank=True, null=True)
    veteran_status = models.CharField(max_length=50, blank=True, null=True)
    count = models.IntegerField()
    year = models.IntegerField()
    sourcefile = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'acsveteran'
