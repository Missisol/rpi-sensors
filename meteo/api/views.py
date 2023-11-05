from rest_framework import viewsets

from meteo.models import BmeData, BmeHistory, DhtData, DhtHistory
from .serializers import BMESerializer, BmeHistorySerializer, DhtDataSerializer, DhtHistorySerializer


class BMEViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides `list`, `create`, `retrieve`, `update` and `destroy` actions.
    """
    queryset = BmeData.objects.all().order_by('-id')
    serializer_class = BMESerializer


class BmeHistoryViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides `list`, `create`, `retrieve`, `update` and `destroy` actions.
    """
    queryset = BmeHistory.objects.all().order_by('-id')
    serializer_class = BmeHistorySerializer


class DhtDataViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides `list`, `create`, `retrieve`, `update` and `destroy` actions.
    """
    queryset = DhtData.objects.all().order_by('-id')
    serializer_class = DhtDataSerializer


class DhtHistoryViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides `list`, `create`, `retrieve`, `update` and `destroy` actions.
    """
    queryset = DhtHistory.objects.all().order_by('-id')
    serializer_class = DhtHistorySerializer
