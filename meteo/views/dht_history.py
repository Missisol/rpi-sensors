from django.views.generic import ListView
from datetime import date, datetime, timedelta
from django.db.models import Max, Min

from meteo.models import Dht1History, Dht2History


class Dht1HistoryView(ListView):
    template_name = "meteo/dht_history.html"
    queryset = Dht1History.objects.order_by("-id")[:10]
    context_object_name = "dht1_history"

class Dht2HistoryView(ListView):
    template_name = "meteo/dht_history.html"
    queryset = Dht2History.objects.order_by("-id")[:10]
    context_object_name = "dht2_history"


class DhtHistoryQuery():
    def get_minmax_dht_date(self, queryObj, queryHistoryObj, n):
        yesterday =  date.today() - timedelta(days=1)
        dht_yesterday_data = queryObj.objects.filter(date=yesterday)
        history_yestarday_data = queryHistoryObj.objects.filter(date=yesterday)
        
        try:
            if dht_yesterday_data.exists() and not history_yestarday_data.exists():
                minmax = dht_yesterday_data.aggregate(
                    Min('temperature'), 
                    Max('temperature'), 
                    Min('humidity'), 
                    Max('humidity'), 
                )
                history = queryHistoryObj(
                    date = yesterday,
                    min_temperature = minmax['temperature__min'], 
                    max_temperature = minmax['temperature__max'], 
                    min_humidity = minmax['humidity__min'], 
                    max_humidity = minmax['humidity__max'],  
                )
                history.save()
                queryObj.objects.filter(date=yesterday).delete()
                print(f'History-{n} saved and DHT yesterday data deleted')
            elif dht_yesterday_data.exists() and history_yestarday_data.exists():
                queryObj.objects.filter(date=yesterday).delete()
                print(f'DHT-{n} yesterday data deleted')
            else:
                print(f'DHT-{n} data has already been deleted')
        except Exception as e:
                print(e)

