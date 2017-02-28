from django.db import models

# Create your models here.

GENDER_CHOICES = (
	('M', 'Male'),
	('F', 'Female'),
	('O', 'Other'),
	('', ''),
	)

APPOINTMENT_TYPE_CHOICES = (
	('N', 'New Patient - Scheduled'),
	('W', 'New Patient - Walk In'),
	('C', 'Check-Up'),
	('R', 'Reprogram, Refit, or Repair'),
	('S', 'Existing Patient - New Sale'),
	)

class Patient(models.Model):
	fname = models.CharField('First Name', max_length=30, blank=True)
	lname = models.CharField('Last Name', max_length=30, blank=True)
	gender = models.CharField('Gender', max_length=1, choices=GENDER_CHOICES, default='')
	phone = models.CharField('Phone Number', max_length=10, blank=True)
	email = models.EmailField('Email Address', blank=True)
	street = models.TextField('Street Address', blank=True)
	city = models.TextField('City', blank=True)
	state = models.CharField('State', max_length=2, blank=True)
	zipcode = models.IntegerField('Zip Code', blank=True, default=0)
	notes = models.TextField('Notes', blank=True)
	createdate = models.DateTimeField('Became a patient on', auto_now_add=True)
	birthday = models.DateField('Birthday', blank=True)

	def getbirthday(self):
		string = '{0:%B} {0:%d}, {0:%Y}'.format(self.birthday)
		return string

	def getname(self):
		return self.fname + " " + self.lname

	def __str__(self):
		return self.fname + " " + self.lname

	def readable_time(self):
		string = '{0:%I}:{0:%M} {0:%p} on {0:%A}, {0:%B} {0:%d}, {0:%Y}'.format(self.createdate)
		return string

class Appointment(models.Model):
	patient = models.ForeignKey('Patient', Patient)
	datetime = models.DateTimeField('Visit Date')
	appttype = models.CharField('Appointment Type', max_length=1, choices=APPOINTMENT_TYPE_CHOICES, default='')
	notes = models.TextField('Description and Notes')

	def readable_time(self):
		string = '{0:%I}:{0:%M} {0:%p} on {0:%A}, {0:%B} {0:%d}, {0:%Y}'.format(self.datetime)
		return string

	def __str__(self):
		return self.patient.getname() + " on " + self.readable_time()


class Manufacturer(models.Model):
	name = models.CharField('Company Name', max_length=30, blank=True)
	phone = models.CharField('Phone Number', max_length=10, blank=True)
	repname = models.CharField('Representative ', max_length=30, blank=True)
	repphone = models.CharField('Phone Number', max_length=10, blank=True)

	def __str__(self):
		return self.name

class Device(models.Model):
	manufacturer = models.ForeignKey('Manufacturer', Manufacturer)
	name = models.CharField('Name', max_length=40, blank=True)
	description = models.TextField('Description', max_length=200)

	def __str__(self):
		return self.name

class OwnedDevice(models.Model):
	device = models.ForeignKey('Device', Device)
	patient = models.ForeignKey('Patient', Patient)
	purchasedate = models.DateTimeField('Purchased on', auto_now_add=True)
	deliverdate = models.DateTimeField('Delivered on')

	def __str__(self):
		return self.device.name


class Audiogram(models.Model):
	patient = models.ForeignKey('Patient', Patient)
	timestamp = models.DateTimeField('Test Date', auto_now_add=True)
	L250  = models.SmallIntegerField('Left 250', default="0")
	L500  = models.SmallIntegerField('Left 500', default="0")
	L1000 = models.SmallIntegerField('Left 1000', default="0")
	L1500 = models.SmallIntegerField('Left 1500', default="0")
	L2000 = models.SmallIntegerField('Left 2000', default="0")
	L3000 = models.SmallIntegerField('Left 3000', default="0")
	L4000 = models.SmallIntegerField('Left 4000', default="0")
	L6000 = models.SmallIntegerField('Left 6000', default="0")
	L8000 = models.SmallIntegerField('Left 8000', default="0")
	R250  = models.SmallIntegerField('Right 250', default="0")
	R500  = models.SmallIntegerField('Right 500', default="0")
	R1000 = models.SmallIntegerField('Right 1000', default="0")
	R1500 = models.SmallIntegerField('Right 1500', default="0")
	R2000 = models.SmallIntegerField('Right 2000', default="0")
	R3000 = models.SmallIntegerField('Right 3000', default="0")
	R4000 = models.SmallIntegerField('Right 4000', default="0")
	R6000 = models.SmallIntegerField('Right 6000', default="0")
	R8000 = models.SmallIntegerField('Right 8000', default="0")
	notes = models.TextField('Notes')

	def get_audio_L(self):
  		return [self.L250, self.L500, self.L1000, self.L1500, self.L2000, self.L3000, self.L4000, self.L6000, self.L8000]

	def get_audio_R(self):
  		return [self.R250, self.R500, self.R1000, self.R1500, self.R2000, self.R3000, self.R4000, self.R6000, self.R8000]

	def readable_time(self):
		string = '{0:%I}:{0:%M} {0:%p} on {0:%A}, {0:%B} {0:%d}, {0:%Y}'.format(self.timestamp)
		return string

	def __str__(self):
		return self.patient.__str__() + " on " + self.readable_time()
