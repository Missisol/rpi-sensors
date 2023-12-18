from django.db import models
import datetime


class Dht1History(models.Model):
    date = models.DateField(default=datetime.date.today)
    min_temperature = models.FloatField()
    max_temperature = models.FloatField()
    min_humidity = models.FloatField()
    max_humidity = models.FloatField()
    def __str__(self):
        return str(self.date)


class Dht2History(models.Model):
    date = models.DateField(default=datetime.date.today)
    min_temperature = models.FloatField()
    max_temperature = models.FloatField()
    min_humidity = models.FloatField()
    max_humidity = models.FloatField()
    def __str__(self):
        return str(self.date)

