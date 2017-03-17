from django.contrib import admin

# Register your models here.
from . import models as m

homeless_models = [m.AgeHouseComposition, m.Disability, m.Ethnicity, 
                   m.GeographicLocation, m.HomelessIndividuals, m.Veterans,
                   m.ChronicHomelessness, m.DomesticViolence, m.SleepingLocation,
                   m.LengthOfHomelessness]


admin.site.register(homeless_models)