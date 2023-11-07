from django.shortcuts import get_object_or_404
from django.views.generic import ListView

from meteo.models import DhtData


class DhtDataView(ListView):
    template_name = "meteo/dht_data.html"
    queryset = DhtData.objects.order_by("-id")[:10]
    context_object_name = "dht_data"