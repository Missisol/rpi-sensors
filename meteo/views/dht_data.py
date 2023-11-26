from django.shortcuts import get_object_or_404
from django.views.generic import ListView

from meteo.models import DhtData
from meteo.modules.sensor_data import dht_data_list

class DhtDataView(ListView):
    template_name = "meteo/dht_data.html"
    queryset = DhtData.objects.order_by("-id")[:10]
    context_object_name = "dht_data"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["data_list"] = dht_data_list
        return context
