from django.contrib import admin
from .models import Patient, Manufacturer, Device, OwnedDevice

# Register your models here.
admin.site.register(Patient)
admin.site.register(Manufacturer)
admin.site.register(Device)
admin.site.register(OwnedDevice)