from django.contrib import admin
from .models import User,Student,Alumni,Faculty,Connections,Opportunities,Emails,Complaints,Event

# Register your models here.
admin.site.register(User)
admin.site.register(Student)
admin.site.register(Alumni)
admin.site.register(Faculty)
admin.site.register(Connections)
admin.site.register(Opportunities)
admin.site.register(Emails)
admin.site.register(Complaints)
admin.site.register(Event)