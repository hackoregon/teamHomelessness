from django.conf.urls import url
from . import views

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Team Homelessness API')

urlpatterns = [
    url(r'^$', schema_view),
    url(r'^disability/$', views.ListDisability.as_view(), name='disability-list'),
    url(r'^ethnicity/$', views.ListEthnicity.as_view(), name='ethnicity-list'),
    url(r'^gender/$', views.ListGender.as_view(), name='gender-list'),
    url(r'^geolocation/$', views.ListGeographiclocation.as_view(), name='geo-list'),
    url(r'^individuals/$', views.ListHomelessindividuals.as_view(), name='individuals-list'),
    url(r'^veterans/$', views.ListVeterans.as_view(), name='veterans-list'),
]