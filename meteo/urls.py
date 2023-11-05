from django.urls import include, path

from meteo.views import bme_data as bme_data_views



urlpatterns = [
  path("api/", include("meteo.api.api_urls")),
  path("", bme_data_views.bme_data, name="bme_data"),
]