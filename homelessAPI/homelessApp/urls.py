from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Team_homelessness_api_root, name='root'),
    url(r'disability/$', views.ListDisability.as_view(), name='disability-list'),
    url(r'^ethnicity/$', views.ListEthnicity.as_view(), name='ethnicity-list'),
    url(r'^gender/$', views.ListGender.as_view(), name='gender-list'),
    url(r'^geolocation/$', views.ListGeographiclocation.as_view(), name='geo-list'),
    url(r'^individuals/$', views.ListHomelessindividuals.as_view(), name='individuals-list'),
    url(r'^veterans/$', views.ListVeterans.as_view(), name='veterans-list'),
]