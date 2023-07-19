from django.contrib import admin
from .models import DeviceType, Controller, Sensor, Proximity

# Register your models here.


@admin.register(DeviceType)
class DeviceTypeAdmin(admin.ModelAdmin):
    list_display = ("title", "description")


@admin.register(Controller)
class ControllerAdmin(admin.ModelAdmin):
    list_display = ("type", "model", "network_address", "unique_id")


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ("model", "type", "controller", "unique_id")


@admin.register(Proximity)
class ProximityAdmin(admin.ModelAdmin):
    list_display = ("sensor", "distance", "timestamp")
