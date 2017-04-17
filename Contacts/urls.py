from django.conf.urls import url
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^$', views.view,name='listContacts'),
    url(r'^view/$', views.viewContacts, name='viewContacts'),
    url(r'^deleteContact/$', views.deleteContact, name='deleteContact'),
]