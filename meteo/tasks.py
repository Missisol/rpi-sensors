from config.celery import app

from meteo.modules.bme_module import BME280Module
from meteo.modules.dht22_module import DHT22Module
from meteo.services import BmeHistoryQuery, DhtHistoryery

bme280_module = BME280Module()
dht22_module = DHT22Module()
history = BmeHistoryQuery()
dhtHistory = DhtHistoryQuery()


@app.task
def get_bme_data():
    bme280_module.get_sensor_readings()


@app.task
def get_bme_history():
    history.get_minmax_bme_date()


@app.task
def get_dht22_data():
    dht22_module.get_dht22_data()


@app.task
def get_dht22_history():
    dhtHistory.get_minmax_dht22_date()
