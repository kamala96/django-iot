from django.contrib import admin
from .models import Proximity

# Register your models here.


@admin.register(Proximity)
class ProximityAdmin(admin.ModelAdmin):
    list_display = ("distance", "timestamp")
