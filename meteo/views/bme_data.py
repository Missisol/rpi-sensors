from django.shortcuts import get_object_or_404
from django.views.generic import ListView

from meteo.models import BmeData
from meteo.utils.sensor_data import bme_data_list


class BmeDataView(ListView):
    template_name = "meteo/bme_data.html"
    queryset = BmeData.objects.order_by("-id")
    context_object_name = "bme_data"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["data_list"] = bme_data_list
        return context
    
        


