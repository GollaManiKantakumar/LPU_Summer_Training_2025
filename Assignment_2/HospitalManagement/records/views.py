from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from records.forms import PatientForm
from records.models import Patient


class PatientCreateView(CreateView):
    model = Patient
    form_class = PatientForm
    template_name = 'records/patient_form.html'  # Correct path
    success_url = reverse_lazy('patient_list')

class PatientUpdateView(UpdateView):
    model = Patient
    form_class = PatientForm
    template_name = 'records/patient_form.html'  # Correct path
    success_url = reverse_lazy('patient_list')

class PatientDeleteView(DeleteView):
    model = Patient
    template_name = 'records/patient_delete.html'  # Correct path
    success_url = reverse_lazy('patient_list')

class PatientListView(ListView):
    model = Patient
    template_name = 'records/patient_list.html'  # Correct path
    context_object_name = 'patients'

class PatientDetailView(DetailView):
    model = Patient
    template_name = 'records/patient_detail.html'  # Correct path
    context_object_name = 'patient'
