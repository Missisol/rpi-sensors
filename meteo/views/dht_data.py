from django.shortcuts import get_object_or_404
from django.views.generic import ListView

from meteo.models import DhtData


class DhtDataView(ListView):
    template_name = "meteo/dht_data.html"
    queryset = DhtData.objects.order_by("-id")[:10]
    context_object_name = "dht_data"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["data_list"] = [
            { 
                'box': [
                    {
                        'dataName': "Температура, &deg;C",
                        'className': 'bx bxs-thermometer readings',
                        'id': 'temperature',
                    }, 
                    {
                        'dataName': "Влажность, %", 
                        'className': 'bx bxs-droplet-half readings readings--two',
                        'id': 'humidity',
                    }, 
                ]
            },
            {
                'gauge': [
                    'temperature',
                    'humidity',
                ]
            }
        ]
        return context
