import smbus2
import bme280
import time
import math
from pytz import timezone
import pytz

from .models import BmeData


class BME280Module:
    PORT = 1
    ADDRESS = 0x76

    
    def __init__(self):
        self.bus = smbus2.SMBus(BME280Module.PORT)
        self.calibration_params = bme280.load_calibration_params(self.bus, BME280Module.ADDRESS)
        
        
    def get_sensor_readings(self):
        sample_reading = bme280.sample(self.bus, BME280Module.ADDRESS, self.calibration_params)
        temperature_val = round(sample_reading.temperature, 1)
        humidity_val = round(sample_reading.humidity, 1)
        pressure_raw_val = sample_reading.pressure
        timestamp_raw_val = sample_reading.timestamp

        # Date calculation 
        utc = pytz.utc
        moscowtz = timezone('Europe/Moscow')
        timestamp_val = timestamp_raw_val.astimezone(moscowtz)
        fmt = '%d-%m-%Y %H:%M:%S'
        current_date = timestamp_val.astimezone(moscowtz).strftime(fmt)

        # Pressure convertion to mmHg
        pressure_val = round(pressure_raw_val * 0.75)

        fm = '%Y-%m-%d'
        dt = timestamp_val.strftime(fm)

        bme = BmeData(temperature = temperature_val, humidity = humidity_val, pressure = pressure_val, full_date = timestamp_val, date = dt)
        bme.save()

        return (temperature_val, pressure_val, humidity_val, timestamp_val)
