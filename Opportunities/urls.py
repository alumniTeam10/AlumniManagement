from django.conf.urls import url
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^$', views.viewOpportunities,name='viewOpportunities'),

    url(r'post/$', views.OpportunityCreate.as_view(),name='postOpportunity'),

    url(r'^(?P<pk>[0-9]+)/$', views.OpportunityUpdate.as_view(),name='updateOpportunity'),

    url(r'^(?P<pk>[0-9]+)/delete/$', views.OpportunityDelete.as_view(),name='deleteOpportunity'),

    url(r'^(?P<pk>[0-9]+)/viewOpportunity/$', views.viewOpportunity, name='viewOpportunity'),

    url(r'^search/$', views.searchOpportunity, name='Opportunitysearch'),


]