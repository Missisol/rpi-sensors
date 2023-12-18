from django.conf import settings
import requests

from meteo.models import Dht1Data, Dht2Data


class DHT22Module:

  def get_dht_data(self):
    try:
        url = settings.DHT_URL
        data = requests.get(url).json()
        tr1 = data['dht1']['temperature']
        hum1 = data['dht1']['humidity']
        tr2 = data['dht2']['temperature']
        hum2 = data['dht2']['humidity']
        # print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(tr, hum))

        if hum1 is not None and tr1 is not None:
            dht22_1 = Dht1Data(temperature = round(tr1, 1), humidity = round(hum1, 1))
            dht22_1.save()
        else:
            print('DHT22_1 error')

        if hum2 is not None and tr2 is not None:
            dht22_2 = Dht2Data(temperature = round(tr2, 1), humidity = round(hum2, 1))
            dht22_2.save()
        else:
            print('DHT22_1 error')

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
    except Exception as error:
        DHT22Sensor.exit()
        raise error

