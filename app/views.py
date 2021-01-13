from django.shortcuts import render

import json
from django.http import JsonResponse
from django.core.serializers import serialize
from .models import Incidentes
from .forms import IncidentesForm

# Create your views here.

def index(request):
	return render(request, 'geoapp/index.html')

def map(request):
	return render(request, 'geoapp/map.html')

def incidentes_view(request):
	incidentes_as_geojson = serialize('geojson', Incidentes.objects.all())
	return JsonResponse(json.loads(incidentes_as_geojson))

def crear_incidente_view(request):
	if request.method == 'POST':
		form = IncidentesForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			message = "Incidente creado!"
	else:
		form = IncidentesForm()

	return render('website/nuevo_incidente.html', locals(), context_instance=RequestContext(request))
