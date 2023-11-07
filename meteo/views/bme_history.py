from django.views.generic import ListView
from datetime import date, datetime, timedelta
from django.db.models import Max, Min

from meteo.models import BmeHistory, BmeData


class BmeHistoryView(ListView):
    template_name = "meteo/bme_history.html"
    queryset = BmeHistory.objects.order_by("-id")[:10]
    context_object_name = "bme_history"


class BmeHistoryQuery():
    yesterday =  date.today() - timedelta(days=1)
    bme_yesterday_data = BmeData.objects.filter(date=yesterday)
    history_yestarday_data = BmeHistory.objects.filter(date=yesterday)

    def delete_yesterday_data(self):
        BmeData.objects.filter(date=self.yesterday).delete()
        print('Deleted BME yesterday data')


    def get_minmax_bme_date(self):
        try:
            if self.bme_yesterday_data and not self.history_yestarday_data:
                minmax = self.bme_yesterday_data.aggregate(
                    Min('temperature'), 
                    Max('temperature'), 
                    Min('humidity'), 
                    Max('humidity'), 
                    Min('pressure'), 
                    Max('pressure')
                )
                history = BmeHistory(
                    date = self.yesterday,
                    min_temperature = minmax['temperature__min'], 
                    max_temperature = minmax['temperature__max'], 
                    min_humidity = minmax['humidity__min'], 
                    max_humidity = minmax['humidity__max'],  
                    min_pressure = minmax['pressure__min'],  
                    max_pressure = minmax['pressure__max'], 
                )
                history.save()
                print('BME History data saved')
                self.delete_yesterday_data()
            elif self.bme_yesterday_data and self.history_yestarday_data:
                # print('Deleted BME yesterday data')
                self.delete_yesterday_data()
            else:
                print('BME data has already been deleted')
        except Exception as e:
                print(e)