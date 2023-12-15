from django.views.generic import ListView
from datetime import date, datetime, timedelta
from django.db.models import Max, Min

from meteo.models import DhtHistory, DhtData


class DhtHistoryView(ListView):
    template_name = "meteo/dht_history.html"
    queryset = DhtHistory.objects.order_by("-id")[:10]
    context_object_name = "dht_history"


class DhtHistoryQuery():
    def get_minmax_dht_data(self):
        yesterday =  date.today() - timedelta(days=1)
        dht_yesterday_data = DhtData.objects.filter(date=yesterday)
        history_yestarday_data = DhtHistory.objects.filter(date=yesterday)

        try:
            if dht_yesterday_data.exists() and not history_yestarday_data.exists():
                minmax = dht_yesterday_data.aggregate(
                    Min('temperature'), 
                    Max('temperature'), 
                    Min('humidity'), 
                    Max('humidity'), 
                )
                history = DhtHistory(
                    date = yesterday,
                    min_temperature = minmax['temperature__min'], 
                    max_temperature = minmax['temperature__max'], 
                    min_humidity = minmax['humidity__min'], 
                    max_humidity = minmax['humidity__max'],  
                )
                history.save()
                DhtData.objects.filter(date=yesterday).delete()
                print('DHT22 history data saved and DHT yesterday data deleted')
            elif dht_yesterday_data.exists() and history_yestarday_data.exists():
                DhtData.objects.filter(date=yesterday).delete()
                print('DHT yesterday data deleted')
            else:
                print('DHT22 data has already been deleted')
        except Exception as e:
                print(e)

