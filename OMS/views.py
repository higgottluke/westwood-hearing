from django.shortcuts import render, get_object_or_404
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from .models import Patient, Audiogram, Appointment
from django.contrib.auth.decorators import login_required
from .forms import NewPatientForm

# Create your views here.
@login_required
def home(request):
	return render(request, 'OMS/home.html', {})

def login(request):
	return render(request, 'OMS/login.html')

def logout(request):
	return render(request, 'OMS/login.html')

@login_required
def calendar(request):
	calendar = Appointment.objects.all()
	return render(request, 'OMS/calendar.html', {'calendar': calendar})

@login_required
def patient_list(request):
	patients = Patient.objects.all().order_by('createdate')
	return render(request, 'OMS/patient_list.html', {'patients': patients})

@login_required
def newpatient(request):
	form = NewPatientForm
	return render(request, 'OMS/newpatient.html', {'form': form})

@login_required
def patient_profile(request, id):
	patient = get_object_or_404(Patient, id=id)
	audiograms = Audiogram.objects.filter(patient__id=id).order_by('timestamp')
	appointments = Appointment.objects.filter(patient__id=id).order_by('datetime')
	return render(request, 'OMS/patient_details.html',
		{'patient': patient,
		'audiograms': audiograms,
		'appointments': appointments,}
	)
