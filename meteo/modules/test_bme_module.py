import smbus2
import bme280
import time
import math
from pytz import timezone
import pytz

from meteo.models import BmeData

import random
from datetime import datetime


class BME280Module:
    PORT = 1
    ADDRESS = 0x76

    
    def __init__(self):
        print('yes')
        # self.bus = smbus2.SMBus(BME280Module.PORT)
        # self.calibration_params = bme280.load_calibration_params(self.bus, BME280Module.ADDRESS)
        
        
    def get_sensor_readings(self):
        # sample_reading = bme280.sample(self.bus, BME280Module.ADDRESS, self.calibration_params)
        # temperature_val = round(sample_reading.temperature, 1)
        # humidity_val = round(sample_reading.humidity, 1)
        # pressure_raw_val = sample_reading.pressure
        # timestamp_raw_val = sample_reading.timestamp
        temperature_val = round(random.uniform(19.0, 23.9), 1)
        humidity_val = round(random.uniform(46.0, 49.9), 1)
        pressure_val = round(random.uniform(743, 760))

        # Date calculation 
        utc = pytz.utc
        moscowtz = timezone('Europe/Moscow')
        # timestamp_val = timestamp_raw_val.astimezone(moscowtz)
        fmt = '%d-%m-%Y %H:%M:%S'
        now = datetime.now()
        print(f'now: {now}')
        dd = now.astimezone(moscowtz)
        print(f'dd: {now.astimezone(moscowtz)}')

        # current_date = dd.astimezone(moscowtz).strftime(fmt)
        # current_date = datetime.timestamp(now).astimezone(moscowtz).strftime(fmt)
        # print(f'curr: {current_date}')

        # Pressure convertion to mmHg
        # pressure_val = round(pressure_raw_val * 0.75)

        fm = '%Y-%m-%d'
        dt = dd.strftime(fm)
        print(f'dt: {dt}')

        bme = BmeData(temperature = temperature_val, humidity = humidity_val, pressure = pressure_val, full_date = dd, date = dt)
        bme.save()

        return (temperature_val, pressure_val, humidity_val, dd)
