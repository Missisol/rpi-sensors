from config.celery import app

from meteo.modules import BME280Module, DHT22Module

from meteo.views.bme_history import BmeHistoryQuery
from meteo.views.dht_history import Dht1HistoryQuery, Dht2HistoryQuery


bme280_module = BME280Module()
dht22_module = DHT22Module()
history = BmeHistoryQuery()
dht1History = Dht1HistoryQuery()
dht2History = Dht2HistoryQuery()


@app.task
def get_bme_data():
    bme280_module.get_sensor_readings()


@app.task
def get_bme_history():
    history.get_minmax_bme_date()


@app.task
def get_dht_data():
    dht22_module.get_dht_data()


@app.task
def get_dht1_history():
    dht1History.get_minmax_dht_date()


@app.task
def get_dht2_history():
    dht2History.get_minmax_dht_date()
