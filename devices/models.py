from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.


class DeviceType(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Device: Types"
        verbose_name_plural = "Device: Types"


class Controller(models.Model):
    type = models.ForeignKey(
        DeviceType, on_delete=models.CASCADE, related_name='type_controllers')
    model = models.CharField(max_length=100)
    network_address = models.GenericIPAddressField()
    chip_id = models.CharField(max_length=100, unique=True)
    access_key = models.CharField(max_length=128, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.type} {self.model} - ChipID#{self.chip_id}'

    def save(self, *args, **kwargs):
        if self._state.adding or 'access_key' in self.get_deferred_fields():
            self.access_key = make_password(self.access_key)
        super(Controller, self).save(*args, **kwargs)


class Sensor(models.Model):
    type = models.ForeignKey(
        DeviceType, on_delete=models.CASCADE, related_name='type_sensors')
    model = models.CharField(max_length=100)
    chip_id = models.CharField(max_length=100, unique=True)
    controller = models.ForeignKey(
        Controller, on_delete=models.CASCADE, related_name='controller_sensors')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.type} {self.model} - ChipID#{self.chip_id}'


class Proximity(models.Model):
    sensor = models.OneToOneField(
        Sensor,
        on_delete=models.CASCADE,
        related_name='sensor_proximity'
    )
    distance = models.DecimalField(max_digits=5, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sensor}: {self.distance} at {self.timestamp}'

    class Meta:
        ordering = ("timestamp", )
        verbose_name = "Proximity"
        verbose_name_plural = "Proximity"
