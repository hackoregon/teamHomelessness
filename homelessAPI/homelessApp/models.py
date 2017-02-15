from django.db import models
from django.contrib.postgres.fields import IntegerRangeField

class Agehousecomposition(models.Model):
    id = models.AutoField(primary_key=True)
    age = IntegerRangeField(null=True)
    householdtype = models.CharField(max_length=255)
    sheltertype = models.CharField(max_length=255)
    count = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    page = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'agehousecomposition'


class Disability(models.Model):
    id = models.AutoField(primary_key=True)
    disabilitytype = models.CharField(max_length=255, blank=True, null=True)
    sheltertype = models.CharField(max_length=255)
    count = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    page = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'disability'


class Ethnicity(models.Model):
    id = models.AutoField(primary_key=True)
    ethnicity = models.CharField(max_length=255, blank=True, null=True)
    sheltertype = models.CharField(max_length=255)
    count = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    page = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'ethnicity'


class Gender(models.Model):
    id = models.AutoField(primary_key=True)
    gender = models.CharField(max_length=255)
    agerange = models.CharField(max_length=255, blank=True, null=True)
    sheltertype = models.CharField(max_length=255)
    count = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    page = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'gender'


class Geographiclocation(models.Model):
    id = models.AutoField(primary_key=True)
    geographiclocation = models.CharField(max_length=255)
    count = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    page = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'geographiclocation'


class Homelessindividuals(models.Model):
    id = models.AutoField(primary_key=True)
    sheltertype = models.CharField(max_length=255)
    age = models.CharField(max_length=255, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    page = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'homelessindividuals'


class Veterans(models.Model):
    id = models.AutoField(primary_key=True)
    veteran = models.CharField(max_length=255, blank=True, null=True)
    sheltertype = models.CharField(max_length=255)
    count = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    page = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'veterans'


class ChronicHomelessness(models.Model):
    id = models.AutoField(primary_key=True)
    chronichomelessnesstype = models.CharField(max_length=255)
    sheltertype = models.CharField(max_length=255)
    count = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    page = models.IntegerField(blank=True, null=True)

    class Meta: 
        db_table = 'chronichomelessness'


class DomesticViolence(models.Model):
    id = models.AutoField(primary_key=True)
    sheltertype = models.CharField(max_length=255)
    count = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    page = models.IntegerField(blank=True, null=True)

    class Meta: 
        db_table = 'domesticviolence'


class SleepingLocation(models.Model):
    id = models.AutoField(primary_key=True)
    sleepinglocation = models.CharField(max_length=255)
    count = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    page = models.IntegerField(blank=True, null=True)

    class Meta: 
        db_table = 'sleepinglocation'


class LengthOfHomelessness(models.Model):
    id = models.AutoField(primary_key=True)
    lengthofhomelessnesstype = models.CharField(max_length=255)
    count = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    page = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'lengthofhomelessness'









