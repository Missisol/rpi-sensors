from django.views.generic import ListView
from datetime import date, datetime, timedelta
from django.db.models import Max, Min

from meteo.models import BmeHistory, BmeData


class BmeHistoryView(ListView):
    template_name = "meteo/bme_history.html"
    queryset = BmeHistory.objects.order_by("-id")[:10]
    context_object_name = "bme_history"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "История BME280"
        return context


class BmeHistoryQuery():
    def get_minmax_bme_data(self):
        for x in range(5, 0, -1):
            yesterday =  date.today() - timedelta(days=x)
            bme_yesterday_data = BmeData.objects.filter(date=yesterday)
            history_yestarday_data = BmeHistory.objects.filter(date=yesterday)

            try:
                if bme_yesterday_data.exists() and not history_yestarday_data.exists():
                    minmax = bme_yesterday_data.aggregate(
                        Min('temperature'), 
                        Max('temperature'), 
                        Min('humidity'), 
                        Max('humidity'), 
                        Min('pressure'), 
                        Max('pressure')
                    )
                    history = BmeHistory(
                        date = yesterday,
                        min_temperature = minmax['temperature__min'], 
                        max_temperature = minmax['temperature__max'], 
                        min_humidity = minmax['humidity__min'], 
                        max_humidity = minmax['humidity__max'],  
                        min_pressure = minmax['pressure__min'],  
                        max_pressure = minmax['pressure__max'], 
                    )
                    history.save()
                    BmeData.objects.filter(date=yesterday).delete()
                    print('BME History data saved and BME yesterday data deleted')
                elif bme_yesterday_data.exists() and history_yestarday_data.exists():
                    BmeData.objects.filter(date=yesterday).delete()
                    print('BME yesterday data deleted')
                else:
                    print('BME data has already been deleted')
            except Exception as e:
                    print(e)