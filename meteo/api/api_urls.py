from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns

# from meteo.api import views
from meteo.api.views import BmeViewSet, BmeLastViewSet, BmeHistoryViewSet, DhtDataViewSet, DhtHistoryViewSet


bme_list =BmeViewSet.as_view({
    'get': 'list',
})
bme_detail =BmeViewSet.as_view({
    'get': 'retrieve',
    'delete': 'destroy',
})
bme_last_list =BmeLastViewSet.as_view({
    'get': 'list',
})
bme_history_list = BmeHistoryViewSet.as_view({
    'get': 'list',
})
bme_history_detail = BmeHistoryViewSet.as_view({
    'get': 'retrieve',
    'delete': 'destroy',
})
dht_list = DhtDataViewSet.as_view({
    'get': 'list',
})
dht_detail = DhtDataViewSet.as_view({
    'get': 'retrieve',
    'delete': 'destroy',
})
dht_history_list = DhtHistoryViewSet.as_view({
    'get': 'list',
})
dht_history_detail = DhtHistoryViewSet.as_view({
    'get': 'retrieve',
    'delete': 'destroy',
})

app_name = 'api'

urlpatterns = [
  path("api/", include('rest_framework.urls', namespace="api"),),
  path('bme/', bme_list, name='bme-list'),
  path('bme/<int:pk>/', bme_detail, name='bme-detail'),
  path('bme-last/', bme_last_list, name='bme-last-list'),
  path('bme-history/', bme_history_list, name='bme-history-list'),
  path('bme-history/<int:pk>/', bme_history_detail, name='bme-history-detail'),
  path('dht/', dht_list, name='dht-list'),
  path('dht/<int:pk>/', dht_detail, name='dht-detail'),
  path('dht-history/', dht_history_list, name='dht-history-list'),
  path('dht-history/<int:pk>/', dht_history_detail, name='dht-history-detail'),
]