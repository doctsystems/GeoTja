from django import forms
from django.views.generic import UpdateView
from leaflet.forms.widgets import LeafletWidget

from .models import Incidentes

class IncidentesForm(forms.ModelForm):
	class Meta:
		model = Incidentes
		fields = '__all__'
		widgets = {'geom': LeafletWidget()}

class EditIncidentes(UpdateView):
	model = Incidentes
	form_class = IncidentesForm
	template_name = 'website/edit_form.html'
