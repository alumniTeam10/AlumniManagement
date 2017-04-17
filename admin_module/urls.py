from django.conf.urls import url
from django.contrib import admin
from . import views


urlpatterns = [
   url(r'^event/$',views.view_event,name='view-event'),
    url(r'^news/$',views.view_news,name='view-news'),
    #admin_module/event/add
    url(r'^event/add/$',views.form_name_view,name='event-add'),
    url(r'^event/(?P<pk>\d+)/delete/$', views.EventDelete.as_view(), name='deleteEvent'),
    url(r'^event/(?P<pk>[0-9]+)/$', views.EventUpdate.as_view(), name='UpdateEvent'),
    url(r'^users/add/$',views.createUser,name='user_name'),
    url(r'^users/(?P<pk>\d+)/delete/$', views.UserDelete.as_view(), name='deleteUser'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserUpdate.as_view(), name='UserUpdate'),
    url(r'^users/$',views.viewUsers,name='view-users'),
    url(r'^search/$', views.searchEvent, name='eventSearch'),
url(r'^search/$', views.searchNews, name='NewsSearch'),
]
