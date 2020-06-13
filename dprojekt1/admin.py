
from django.contrib.gis import admin
from .models import Rury, Armatura, Hydranty
from leaflet.admin import LeafletGeoAdmin


class RuryAdmin(LeafletGeoAdmin):
    list_display = ('id', 'objectid', 'gn_last_ed', 'main_funct','diameter', 'gn_last_ed','gn_creat_1', 'mpoly')

class ArmaturaAdmin(LeafletGeoAdmin):
    list_display = ('id', 'objectid', 'diameter_n', 'height','covering', 'location','gn_last_ed', 'gn_creat_1','mpoly')

class HydrantyAdmin(LeafletGeoAdmin):
    list_display = ('id', 'objectid', 'location', 'gn_last_ed','gn_creat_1', 'mpoly')

admin.site.register(Rury, RuryAdmin)
admin.site.register(Armatura, ArmaturaAdmin)
admin.site.register(Hydranty, HydrantyAdmin)
# Register your models here.
