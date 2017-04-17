from django.conf.urls import include,url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from  django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'home'},name='logout'),
    url(r'Database/',include('Database.urls')),
    url(r'^$', include('Connect.urls')),
    url(r'Connect/', include('Connect.urls')),
    url(r'Contacts/', include('Contacts.urls')),
    url(r'ManageProfile/', include('ManageProfile.urls')),
    url(r'Opportunity/', include('Opportunities.urls')),
    url(r'Complaints/', include('Complaints.urls')),
    url(r'admin_module/',include('admin_module.urls')),
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)