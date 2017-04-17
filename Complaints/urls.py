from django.conf.urls import url
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^$', views.viewComplaints,name='viewComplaints'),

    url(r'post/$', views.ComplaintCreate.as_view(),name='postComplaint'),

    url(r'^(?P<pk>[0-9]+)/$', views.ComplaintUpdate.as_view(),name='updateComplaint'),

    url(r'^(?P<pk>[0-9]+)/delete/$', views.ComplaintDelete.as_view(),name='deleteComplaint'),

    url(r'^(?P<pk>[0-9]+)/viewComplaint/$', views.viewComplaint, name='viewComplaint'),

    url(r'^search/$', views.searchComplaint, name='Complaintsearch'),


]