from django.conf.urls import url
from django.contrib import admin
from . import views


urlpatterns = [

    url(r'^$', views.home,name='home'),
    url(r'^about$', views.about,name='about'),
    url(r'^contact_us', views.contact_us,name='contact_us'),

    url(r'^(student|faculty|alumni)/$', views.connect,name='connect'),
    url(r'^(student|faculty|alumni)/search/$', views.search, name='search'),

    url(r'^(student|faculty|alumni)/view/$', views.view, name='view'),

    url(r'^(student|faculty|alumni)/addToContact/$', views.add_to_contacts, name='add_to_contacts'),
    url(r'^(student|faculty|alumni)/deleteContact/$', views.delete_contact, name='delete_contact'),
]