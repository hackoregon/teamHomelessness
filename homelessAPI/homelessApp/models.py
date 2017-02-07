from django.db import models

class Agehousecomposition(models.Model):
    age = models.CharField(max_length=255)
    householdtype = models.CharField(max_length=255)
    sheltertype = models.CharField(max_length=255)
    propyes = models.FloatField(blank=True, null=True)
    propno = models.FloatField(blank=True, null=True)
    countyes = models.IntegerField(blank=True, null=True)
    countno = models.IntegerField(blank=True, null=True)
    yearinpit = models.IntegerField(blank=True, null=True)
    pageinpit = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'agehousecomposition'


class Disability(models.Model):
    disabilitytype = models.CharField(max_length=255, blank=True, null=True)
    sheltertype = models.CharField(max_length=255)
    count = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    page = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'disability'


class Ethnicity(models.Model):
    ethnicity = models.CharField(max_length=255, blank=True, null=True)
    sheltertype = models.CharField(max_length=255)
    count = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    page = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'ethnicity'


class Gender(models.Model):
    gender = models.CharField(max_length=255)
    agerange = models.CharField(max_length=255, blank=True, null=True)
    sheltertype = models.CharField(max_length=255)
    count = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    page = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'gender'


class Geographiclocation(models.Model):
    geographiclocation = models.CharField(max_length=255)
    count = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    page = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'geographiclocation'


class Homelessindividuals(models.Model):
    sheltertype = models.CharField(max_length=255)
    age = models.CharField(max_length=255, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    page = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'homelessindividuals'


class Veterans(models.Model):
    veteran = models.CharField(max_length=255, blank=True, null=True)
    sheltertype = models.CharField(max_length=255)
    count = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    page = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'veterans'
