import board
import adafruit_dht

from meteo.models import DhtData

import random


class DHT22Module:
#   DHT22Sensor = adafruit_dht.DHT22(board.D18, use_pulseio=False)

  def get_dht_data(self):
    try:
        # Print the values to the serial port
        # tr = self.DHT22Sensor.temperature
        # hum = self.DHT22Sensor.humidity
        tr = round(random.uniform(19.0, 23.9), 1)
        hum = round(random.uniform(46.0, 49.9), 1)

        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(tr, hum))

        if hum is not None and tr is not None:
            dht22 = DhtData(temperature = round(tr, 1), humidity = round(hum, 1))
            dht22.save()
        else:
            print('DHT22 error')

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
    except Exception as error:
        # DHT22Sensor.exit()
        raise error
