from django.conf.urls import url
from . import views

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Team Homelessness API')

urlpatterns = [
    url(r'^$', schema_view),
    url(r'^disability/$', views.ListDisability.as_view()),
    url(r'^ethnicity/$', views.ListEthnicity.as_view()),
    url(r'^gender/$', views.ListGender.as_view()),
    url(r'^geolocation/$', views.ListGeographiclocation.as_view()),
    url(r'^individuals/$', views.ListHomelessindividuals.as_view()),
    url(r'^veterans/$', views.ListVeterans.as_view()),
    url(r'^sleeping/$', views.ListSleepingLocation.as_view()),
    url(r'^length/$', views.ListLengthOfHomelessness.as_view()),
    url(r'^domesticviolence/$', views.ListDomesticViolence.as_view()),
    url(r'^chronic/$', views.ListChronicHomelessness.as_view()),
    url(r'^agehousecomp/$', views.ListChronicHomelessness.as_view()),
    url(r'^acsage/$', views.ListAcsage.as_view()),
    url(r'^acsdisability/$', views.ListAcsdisability.as_view()),
    url(r'^acsrace/$', views.ListAcsrace.as_view()),
    url(r'^acsveteran/$', views.ListAgeHouseComp.as_view()),
]
