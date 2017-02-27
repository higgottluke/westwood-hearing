from django.contrib import admin
from .models import Patient, Manufacturer, Device, OwnedDevice, Audiogram, Appointment

# Register your models here.
admin.site.register(Patient)
admin.site.register(Manufacturer)
admin.site.register(Device)
admin.site.register(OwnedDevice)
admin.site.register(Audiogram)
admin.site.register(Appointment)
