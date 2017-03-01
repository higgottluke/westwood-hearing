from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Patient, Audiogram, Appointment
from django.contrib.auth.decorators import login_required
from .forms import PatientForm

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
	if request.method == 'POST':
		form = PatientForm(request.POST)
		if form.is_valid():
			# do something to create a new Patient object
			form.save()
			return redirect('/patients')
	else:
		form = PatientForm
		return render(request, 'OMS/newpatient.html', {'form': form})

@login_required
def patient_profile(request, id):
	patient = get_object_or_404(Patient, id=id)
	if request.method == 'POST':
		form = PatientForm(request.POST, instance=patient)
		if form.is_valid():
			# do something to create a new Patient object
			form.save()
			return redirect('/patients')
		else:
			return redirect('/')
	else:
		form = PatientForm(instance=patient)
		audiograms = Audiogram.objects.filter(patient__id=id).order_by('timestamp')
		appointments = Appointment.objects.filter(patient__id=id).order_by('datetime')
		return render(request, 'OMS/patient_details.html', {
			'patient': patient,
			'audiograms': audiograms,
			'appointments': appointments,
			'patientform': form,
			}
		)
