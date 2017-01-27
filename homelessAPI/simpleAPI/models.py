# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

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
        managed = False
        db_table = 'agehousecomposition'


class Ethnicity(models.Model):
    ethnicity = models.CharField(max_length=255, blank=True, null=True)
    sheltertype = models.CharField(max_length=255)
    propyes = models.FloatField(blank=True, null=True)
    propno = models.FloatField(blank=True, null=True)
    countyes = models.IntegerField(blank=True, null=True)
    countno = models.IntegerField(blank=True, null=True)
    yearinpit = models.IntegerField(blank=True, null=True)
    pageinpit = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ethnicity'


class Gender(models.Model):
    gender = models.CharField(max_length=255)
    agerange = models.CharField(max_length=255, blank=True, null=True)
    sheltertype = models.CharField(max_length=255)
    propyes = models.FloatField(blank=True, null=True)
    propno = models.FloatField(blank=True, null=True)
    countyes = models.IntegerField(blank=True, null=True)
    countno = models.IntegerField(blank=True, null=True)
    yearinpit = models.IntegerField(blank=True, null=True)
    pageinpit = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gender'


class Geographiclocation(models.Model):
    geographiclocation = models.CharField(max_length=255)
    count_geographicloc = models.IntegerField(blank=True, null=True)
    prop_geographicloc = models.FloatField(blank=True, null=True)
    yearinpit = models.IntegerField(blank=True, null=True)
    pageinpit = models.IntegerField(blank=True, null=True)
    total_used_in_calculations = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'geographiclocation'


class Homelessindividuals(models.Model):
    sheltertype = models.CharField(max_length=255)
    age = models.CharField(max_length=255)
    propyes = models.FloatField(blank=True, null=True)
    propno = models.FloatField(blank=True, null=True)
    countyes = models.IntegerField(blank=True, null=True)
    countno = models.IntegerField(blank=True, null=True)
    yearinpit = models.IntegerField(blank=True, null=True)
    pageinpit = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'homelessindividuals'


class Veterans(models.Model):
    veteran = models.CharField(max_length=255, blank=True, null=True)
    sheltertype = models.CharField(max_length=255)
    multnomahgeneraladultpoppercveterans = models.FloatField(blank=True, null=True)
    multnomahadultpopcolorpercveterans = models.FloatField(blank=True, null=True)
    chronichomelesspercveterans = models.FloatField(blank=True, null=True)
    propyes = models.FloatField(blank=True, null=True)
    propno = models.FloatField(blank=True, null=True)
    countyes = models.IntegerField(blank=True, null=True)
    countno = models.IntegerField(blank=True, null=True)
    yearinpit = models.IntegerField(blank=True, null=True)
    pageinpit = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'veterans'



        