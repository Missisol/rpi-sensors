from django.views.generic import ListView
from datetime import date, datetime, timedelta
from django.db.models import Max, Min

from meteo.models import Dht1History, Dht1Data, Dht2History, Dht2Data


class Dht1HistoryView(ListView):
    template_name = "meteo/dht_history.html"
    queryset = Dht1History.objects.order_by("-id")[:10]
    context_object_name = "dht1_history"

class Dht2HistoryView(ListView):
    template_name = "meteo/dht_history.html"
    queryset = Dht2History.objects.order_by("-id")[:10]
    context_object_name = "dht1_history"


class Dht1HistoryQuery():
    def get_minmax_dht_date(self):
        yesterday =  date.today() - timedelta(days=1)
        dht_yesterday_data = Dht1Data.objects.filter(date=yesterday)
        history_yestarday_data = Dht1History.objects.filter(date=yesterday)
        
        try:
            if dht_yesterday_data.exists() and not history_yestarday_data.exists():
                minmax = dht_yesterday_data.aggregate(
                    Min('temperature'), 
                    Max('temperature'), 
                    Min('humidity'), 
                    Max('humidity'), 
                )
                history = Dht1History(
                    date = yesterday,
                    min_temperature = minmax['temperature__min'], 
                    max_temperature = minmax['temperature__max'], 
                    min_humidity = minmax['humidity__min'], 
                    max_humidity = minmax['humidity__max'],  
                )
                history.save()
                Dht1Data.objects.filter(date=yesterday).delete()
                print('DHT22-1 history data saved and DHT yesterday data deleted')
            elif dht_yesterday_data.exists() and history_yestarday_data.exists():
                Dht1Data.objects.filter(date=yesterday).delete()
                print('DHT22-1 yesterday data deleted')
            else:
                print('DHT22-1 data has already been deleted')
        except Exception as e:
                print(e)

class Dht2HistoryQuery():
    def get_minmax_dht_date(self):
        yesterday =  date.today() - timedelta(days=1)
        dht_yesterday_data = Dht2Data.objects.filter(date=yesterday)
        history_yestarday_data = Dht2History.objects.filter(date=yesterday)
        
        try:
            if dht_yesterday_data.exists() and not history_yestarday_data.exists():
                minmax = dht_yesterday_data.aggregate(
                    Min('temperature'), 
                    Max('temperature'), 
                    Min('humidity'), 
                    Max('humidity'), 
                )
                history = Dht2History(
                    date = yesterday,
                    min_temperature = minmax['temperature__min'], 
                    max_temperature = minmax['temperature__max'], 
                    min_humidity = minmax['humidity__min'], 
                    max_humidity = minmax['humidity__max'],  
                )
                history.save()
                Dht2Data.objects.filter(date=yesterday).delete()
                print('DHT22-2 history data saved and DHT yesterday data deleted')
            elif dht_yesterday_data.exists() and history_yestarday_data.exists():
                Dht2Data.objects.filter(date=yesterday).delete()
                print('DHT22-2 yesterday data deleted')
            else:
                print('DHT22-2 data has already been deleted')
        except Exception as e:
                print(e)

