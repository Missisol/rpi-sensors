from django.db import models
import datetime


class BmeHistory(models.Model):
    date = models.DateField(default=datetime.date.today)
    min_temperature = models.FloatField()
    max_temperature = models.FloatField()
    min_humidity = models.FloatField()
    max_humidity = models.FloatField()
    min_pressure = models.IntegerField()
    max_pressure = models.IntegerField()
    def __str__(self):
        return str(self.date)

