from django.db import models
import datetime


class BmeData(models.Model):
    temperature = models.FloatField()
    humidity = models.FloatField()
    pressure = models.IntegerField()
    full_date = models.DateTimeField(db_column='date time')
    date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.full_date.strftime('%Y-%m-%d %H:%M:%S')
