from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import PatientForm, ContactForm
from .models import Patient, Audiogram, Appointment

def home(request):
	form_class = ContactForm
	if request.method == 'POST':
		form = form_class(data=request.POST)
		if form.is_valid():
			contact_name = request.POST.get('contact_name', '')
			contact_email = request.POST.get('contact_email', '')
			form_subject = request.POST.get('subject', '')
			form_content = request.POST.get('content', '')

			template = get_template('OMS/contact_template.html')
			context = Context({
				'contact_name': contact_name,
				'contact_email': contact_email,
				'form_content': form_content,
				})
			content = template.render(context)

			email_to_office = EmailMessage(
				"New Contact Form Submission",
				content,
				'info@westwoodhearing.com',
				['info@westwoodhearing.com',],
				reply_to=[contact_email]
				)
			email_to_office.content_subtype = "html"
			email_to_office.send()
			email_to_them = EmailMessage(
				"Thanks for the message!",
				"<p>This is what you sent us:</p>" + content + "<p>Our team will answer as soon as we can.</p>",
				'info@westwoodhearing.com',
				[contact_email],
				reply_to=['info@westwoodhearing.com']
				)
			email_to_them.content_subtype = "html"
			email_to_them.send()

			messages.add_message(request, messages.SUCCESS, "Your message was sent successfully! Our team will answer as soon as they can. You should receive a copy of your message at your email address soon.")
			return redirect('/')
		else:
			messages.add_message(request, messages.WARNING, "Something went wrong. Try filling the form out again, or send us an email directly at info@westwoodhearing.com")
			return redirect('/')

	return render(request, 'OMS/external.html')


# Create your views here.
@login_required
def patients(request):
	patients = Patient.objects.all().order_by('lname')
	return render(request, 'OMS/home.html', {'patients': patients})

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
			messages.add_message(request, messages.ERROR, 'Unexpected Error')
			return redirect('/patient/')
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
			return redirect('/patient/{}/'.format(form.fields['id']))
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
@login_required
def audiogram(request, id):
	audiogram = Audiogram.objects.get(id=id)
	return render(request, 'OMS/audiogram.html', {
		'audiogram': audiogram,
		'patient': audiogram.patient,
		})
