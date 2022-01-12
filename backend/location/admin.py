from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from . models import location

@admin.register(location)
class locationAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')

# Register your models here.
