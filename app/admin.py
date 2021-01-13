from leaflet.admin import LeafletGeoAdmin
from django.contrib import admin
from .models import *
# Register your models here.
# class IncidentesAdmin(LeafletGeoAdmin):
# 	#pass
# 	list_display =('fecha','descripcion', 'lista_tags')
# 	search_fields = ['tag', 'fecha']
# 	list_filter = ('estado', 'fecha_back')
	#fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

admin.site.register(Categorias)
admin.site.register(Tag)
# admin.site.register(Incidentes, IncidentesAdmin)
admin.site.register(Incidentes)