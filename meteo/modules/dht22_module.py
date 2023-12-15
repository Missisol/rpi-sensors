from django.conf import settings
import requests

from meteo.models import DhtData


class DHT22Module:

  def get_dht_data(self):
    try:
        url = settings.DHT_URL
        data = requests.get(url).json()
        tr = data['temperature']
        hum = data['humidity']
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
        DHT22Sensor.exit()
        raise error

