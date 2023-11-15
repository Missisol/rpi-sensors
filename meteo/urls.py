from django.urls import include, path

from meteo.views.bme_data import BmeDataView
from meteo.views.bme_history import BmeHistoryView
from meteo.views.dht_data import DhtDataView
from meteo.views.dht_history import DhtHistoryView

urlpatterns = [
  path("api/", include("meteo.api.api_urls")),
  path("bme/", BmeDataView.as_view(), name="bme"),
  path("bme-history/", BmeHistoryView.as_view(), name="bme-history"),
  path("dht/", DhtDataView.as_view(), name="dht"),
  path("dht-history/", DhtHistoryView.as_view(), name="dht-history"),
]