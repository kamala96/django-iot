from django.db import models

# Create your models here.


class DeviceType:
    title = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    description = models.TextField(max_length=200)


class Controllers:
    address = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=100, unique=True)


class Proximity(models.Model):
    distance = models.DecimalField(max_digits=5, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.distance} at {self.timestamp}'

    class Meta:
        ordering = ("timestamp", )
        verbose_name = "Proximity"
        verbose_name_plural = "Proximity"
