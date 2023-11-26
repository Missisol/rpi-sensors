from django.shortcuts import get_object_or_404
from django.views.generic import ListView

from meteo.models import BmeData, DhtData


class BmeDataView(ListView):
    template_name = "meteo/bme_data.html"
    queryset = BmeData.objects.order_by("-id")
    context_object_name = "bme_data"

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
                    {
                        'dataName': "Давление, мм.рт.ст.", 
                        'className': 'bx bxs-tachometer readings readings--three',
                        'id': 'pressure',
                    },
                ]
            },
            {
                'gauge': [
                    'temperature',
                    'humidity',
                    'pressure',
                ]
            }
        ]
        return context
    
        


