from django.db import models
from django.utils import timezone

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor(models.Model):
    name = models.CharField(max_length=64)
    discription = models.CharField(max_length=256)

class Measurement(models.Model):
    id_sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurement')
    temperature = models.DecimalField(decimal_places=1)
    created_at = models.DateTimeField(auto_now_add=timezone.now())