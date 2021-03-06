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


class HomelessMigration(models.Model):
    migrationarea = models.CharField(max_length=255)
    migrationpercent = models.FloatField()

    class Meta:
        db_table = 'homelessmigration'
        verbose_name_plural = 'Homeless Migration'

# ------------------------------------------------------------------
# ACS models

class Pitacscomp(models.Model):
    comp_name = models.CharField(max_length=255)
    pit_percent = models.FloatField()
    acs_percent = models.FloatField()

    class Meta:
        db_table = 'pitacscomp'

class Pitacsethcomp(models.Model):
    ethnicity = models.CharField(max_length=255)
    hud_homeless = models.FloatField(blank=True, null=True)
    mult_poverty = models.FloatField(blank=True, null=True)
    mult_general = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'pitacsethcomp'

# ------------------------------------------------------------------
# acs models below aren't currently being used in favor of the ones above
class Acsage(models.Model):
    acsid = models.CharField(max_length=1000, blank=True, null=True)
    geoid = models.CharField(max_length=255, blank=True, null=True)
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

# ------------------------------------------------------------------------
# 211 data 

class BinnedAge211(models.Model):
    age_range = IntegerRangeField()
    freq = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'binned_age_211'


class Gender211(models.Model):
    gender = models.CharField(max_length=255, blank=True, null=True)
    freq = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'gender_211'


class Military211(models.Model):
    status = models.CharField(max_length=255, blank=True, null=True)
    freq = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'military_211'


class MonthDemand211(models.Model):
    month = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    freq = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'month_demand_211'


class Service211(models.Model):
    service_name = models.CharField(max_length=255, blank=True, null=True)
    freq = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'service_211'