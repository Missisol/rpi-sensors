from django.views.generic import ListView
from datetime import date, datetime, timedelta
from django.db.models import Max, Min

from meteo.models import DhtHistory, DhtData


class DhtHistoryView(ListView):
    template_name = "meteo/dht_history.html"
    queryset = DhtHistory.objects.order_by("-id")[:10]
    context_object_name = "dht_history"


class DhtHistoryQuery():
    yesterday =  date.today() - timedelta(days=1)
    dht_yesterday_data = DhtData.objects.filter(date=yesterday)
    history_yestarday_data = DhtHistory.objects.filter(date=yesterday)

    def delete_yesterday_data(self):
        DhtData.objects.filter(date=self.yesterday).delete()
        print('Deleted DHT22 yesterday data')


    def get_minmax_dht_date(self):
        try:
            if self.dht_yesterday_data and not self.history_yestarday_data:
                minmax = self.dht_yesterday_data.aggregate(
                    Min('temperature'), 
                    Max('temperature'), 
                    Min('humidity'), 
                    Max('humidity'), 
                )
                history = DhtHistory(
                    date = self.yesterday,
                    min_temperature = minmax['temperature__min'], 
                    max_temperature = minmax['temperature__max'], 
                    min_humidity = minmax['humidity__min'], 
                    max_humidity = minmax['humidity__max'],  
                )
                history.save()
                print('DHT22 history data saved')
                self.delete_yesterday_data()
            elif self.dht_yesterday_data and self.history_yestarday_data:
                self.delete_yesterday_data()
            else:
                print('DHT22 data has already been deleted')
        except Exception as e:
                print(e)

