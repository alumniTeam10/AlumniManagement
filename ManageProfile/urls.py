from django.conf.urls import url
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^$', views.view,name='view'),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.ProfileUpdate.as_view(), name='editProfile'),
]