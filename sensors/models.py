from django.db import models

class Sensor(models.Model):
    SENSOR_TYPES = [
        ('AQ', 'Air Quality'),
        ('TEMP', 'Temperature'),
    ]
    
    type = models.CharField(max_length=50, choices=SENSOR_TYPES)
    model = models.CharField(max_length=100)
    installation_date = models.DateField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.model} ({self.get_type_display()})'

class Data(models.Model):
    sensor = models.ForeignKey(Sensor, related_name='data', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    pm25 = models.FloatField()
    pm10 = models.FloatField()
    co2 = models.FloatField()

    def __str__(self):
        return f'{self.sensor} - {self.timestamp}'

class Alert(models.Model):
    sensor = models.ForeignKey(Sensor, related_name='alerts', on_delete=models.CASCADE)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Alert: {self.description} - {self.timestamp}'
