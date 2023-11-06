from django.urls import include, path

from meteo.views.bme_data import BmeDataView

urlpatterns = [
  path("api/", include("meteo.api.api_urls")),
  path("", BmeDataView.as_view()),
]