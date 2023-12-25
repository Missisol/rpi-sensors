from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns

# from meteo.api import views
from meteo.api.views import BmeViewSet, BmeLastViewSet, BmeHistoryViewSet, Dht1ViewSet, Dht1LastViewSet, Dht1HistoryViewSet, Dht2ViewSet, Dht2LastViewSet, Dht2HistoryViewSet


bme_list = BmeViewSet.as_view({
    'get': 'list',
})
bme_detail = BmeViewSet.as_view({
    'get': 'retrieve',
    'delete': 'destroy',
})
bme_last_list = BmeLastViewSet.as_view({
    'get': 'list',
})
bme_history_list = BmeHistoryViewSet.as_view({
    'get': 'list',
})
bme_history_detail = BmeHistoryViewSet.as_view({
    'get': 'retrieve',
    'delete': 'destroy',
})
dht1_list = Dht1ViewSet.as_view({
    'get': 'list',
})
dht1_detail = Dht1ViewSet.as_view({
    'get': 'retrieve',
    'delete': 'destroy',
})
dht1_last_list = Dht1LastViewSet.as_view({
    'get': 'list',
})
dht1_history_list = Dht1HistoryViewSet.as_view({
    'get': 'list',
})
dht1_history_detail = Dht1HistoryViewSet.as_view({
    'get': 'retrieve',
    'delete': 'destroy',
})
dht2_list = Dht2ViewSet.as_view({
    'get': 'list',
})
dht2_detail = Dht2ViewSet.as_view({
    'get': 'retrieve',
    'delete': 'destroy',
})
dht2_last_list = Dht2LastViewSet.as_view({
    'get': 'list',
})
dht2_history_list = Dht2HistoryViewSet.as_view({
    'get': 'list',
})
dht2_history_detail = Dht2HistoryViewSet.as_view({
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
  path('dht1/', dht1_list, name='dht1-list'),
  path('dht1/<int:pk>/', dht1_detail, name='dht1-detail'),
  path('dht1-last/', dht1_last_list, name='dht1-last-list'),
  path('dht1-history/', dht1_history_list, name='dht1-history-list'),
  path('dht1-history/<int:pk>/', dht1_history_detail, name='dht1-history-detail'),
  path('dht2/', dht2_list, name='dht2-list'),
  path('dht2/<int:pk>/', dht2_detail, name='dht2-detail'),
  path('dht2-last/', dht2_last_list, name='dht2-last-list'),
  path('dht2-history/', dht2_history_list, name='dht2-history-list'),
  path('dht2-history/<int:pk>/', dht2_history_detail, name='dht2-history-detail'),
]