from config.celery import app

from meteo.modules import BME280Module, DHT22Module
from meteo.views.bme_history import BmeHistoryQuery
from meteo.views.dht_history import DhtHistoryQuery
from meteo.models import Dht1Data, Dht1History, Dht2Data, Dht2History



bme280_module = BME280Module()
dht22_module = DHT22Module()
history = BmeHistoryQuery()
dhtHistory = DhtHistoryQuery()


@app.task
def get_bme_data():
    bme280_module.get_sensor_readings()


@app.task
def get_bme_history():
    history.get_minmax_bme_data()


@app.task
def get_dht_data():
    dht22_module.get_dht_data()


@app.task
def get_dht_history():
    dhtHistory.get_minmax_dht_data(Dht1Data, Dht1History, 1)
    dhtHistory.get_minmax_dht_data(Dht2Data, Dht2History, 2)
