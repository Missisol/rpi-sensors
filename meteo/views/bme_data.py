from django.shortcuts import get_object_or_404
from django.views.generic import ListView

from meteo.models import BmeData


class BmeDataView(ListView):
    template_name = "meteo/bme_data.html"
    queryset = BmeData.objects.order_by("-id")[:10]
    context_object_name = "bme_data"

        


