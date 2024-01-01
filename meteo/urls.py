from django.urls import include, path

from meteo.views.bme_data import BmeDataView
from meteo.views.bme_history import BmeHistoryView
from meteo.views.dht_data import Dht1DataView, Dht2DataView
from meteo.views.dht_history import Dht1HistoryView, Dht2HistoryView

from meteo.views.home import HomePageView

urlpatterns = [
  path("api/", include("meteo.api.api_urls")),
  path("", HomePageView.as_view(), name="home"),
  path("bme/", BmeDataView.as_view(), name="bme"),
  path("bme-history/", BmeHistoryView.as_view(), name="bme-history"),
  path("dht1/", Dht1DataView.as_view(), name="dht1"),
  path("dht1-history/", Dht1HistoryView.as_view(), name="dht1-history"),
  path("dht2/", Dht2DataView.as_view(), name="dht2"),
  path("dht2-history/", Dht2HistoryView.as_view(), name="dht2-history"),
]