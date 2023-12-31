from django.db import models
import datetime


class Dht1Data(models.Model):
    full_date = models.DateTimeField(auto_now_add=True, db_column='date time')
    date = models.DateField(default=datetime.date.today)
    temperature = models.FloatField()
    humidity = models.FloatField()
    def __str__(self):
        return str(self.temperature)


class Dht2Data(models.Model):
    full_date = models.DateTimeField(auto_now_add=True, db_column='date time')
    date = models.DateField(default=datetime.date.today)
    temperature = models.FloatField()
    humidity = models.FloatField()
    def __str__(self):
        return str(self.temperature)
