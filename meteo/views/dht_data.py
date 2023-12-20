from django.shortcuts import get_object_or_404
from django.views.generic import ListView

from meteo.models import Dht1Data, Dht2Data
from meteo.utils.sensor_data import data_list


class Dht1DataView(ListView):
    template_name = "meteo/dht_data.html"
    queryset = Dht1Data.objects.order_by("-id")[:10]
    context_object_name = "dht1_data"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["data_list"] = data_list
        context['page_title'] = "Данные DHT22-1"
        return context

        
class Dht2DataView(ListView):
    template_name = "meteo/dht_data.html"
    queryset = Dht2Data.objects.order_by("-id")[:10]
    context_object_name = "dht2_data"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["data_list"] = data_list
        context['page_title'] = "Данные DHT22-2"
        return context
