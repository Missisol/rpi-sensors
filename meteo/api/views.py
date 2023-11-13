from rest_framework import viewsets

from meteo.models import BmeData, BmeHistory, DhtData, DhtHistory
from .serializers import BmeSerializer, BmeHistorySerializer, DhtDataSerializer, DhtHistorySerializer


class BmeViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides `list`, `create`, `retrieve`, `update` and `destroy` actions.
    """
    queryset = BmeData.objects.all().order_by('-id')
    serializer_class = BmeSerializer


class BmeLastViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides `list`, `create`, `retrieve`, `update` and `destroy` actions.
    """
    queryset = BmeData.objects.all().order_by('-id')[:1]
    serializer_class = BmeSerializer


class BmeHistoryViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides `list`, `create`, `retrieve`, `update` and `destroy` actions.
    """
    queryset = BmeHistory.objects.all().order_by('-id')
    serializer_class = BmeHistorySerializer


class DhtViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides `list`, `create`, `retrieve`, `update` and `destroy` actions.
    """
    queryset = DhtData.objects.all().order_by('-id')
    serializer_class = DhtDataSerializer


class DhtLastViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides `list`, `create`, `retrieve`, `update` and `destroy` actions.
    """
    queryset = DhtData.objects.all().order_by('-id')[:1]
    serializer_class = DhtDataSerializer


class DhtHistoryViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides `list`, `create`, `retrieve`, `update` and `destroy` actions.
    """
    queryset = DhtHistory.objects.all().order_by('-id')
    serializer_class = DhtHistorySerializer
