from django.db import models

# Create your models here.

GENDER_CHOICES = (
	('M', 'Male'),
	('F', 'Female'),
	('O', 'Other'),
	('', ''),
	)

class Patient(models.Model):
	fname = models.CharField('First Name', max_length=30, default=" ")
	lname = models.CharField('Last Name', max_length=30, default=" ")
	gender = models.CharField('Gender', max_length=1, choices=GENDER_CHOICES, default='')
	phone = models.CharField('Phone Number', max_length=10, default=" ")
	email = models.EmailField('Email Address', default=" ")

	def __str__(self):
		return self.fname + " " + self.lname

class Manufacturer(models.Model):
	name = models.CharField('Company Name', max_length=30, default=" ")
	phone = models.CharField('Phone Number', max_length=10, default=" ")
	repname = models.CharField('Representative ', max_length=30, default=" ")
	repphone = models.CharField('Phone Number', max_length=10, default=" ")

class Device(models.Model):
	manufacturer = models.ForeignKey('Manufacturer', Manufacturer)
	name = models.CharField('Name', max_length=40, default=" ")
	description = models.TextField('Description', max_length=200)

class OwnedDevice(models.Model):
	device = models.ForeignKey('Device', Device)
	patient = models.ForeignKey('Patient', Patient)
	purchasedate = models.DateTimeField('Purchased on', auto_now_add=True)
	deliverdate = models.DateTimeField();