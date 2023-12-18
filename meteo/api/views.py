from rest_framework import viewsets

from meteo.models import BmeData, BmeHistory, Dht1Data, Dht1History, Dht2Data, Dht2History
from .serializers import BmeSerializer, BmeHistorySerializer, Dht1DataSerializer, Dht1HistorySerializer, Dht2DataSerializer, Dht2HistorySerializer


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


class Dht1ViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides `list`, `create`, `retrieve`, `update` and `destroy` actions.
    """
    queryset = Dht1Data.objects.all().order_by('-id')
    serializer_class = Dht1DataSerializer


class Dht1LastViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides `list`, `create`, `retrieve`, `update` and `destroy` actions.
    """
    queryset = Dht1Data.objects.all().order_by('-id')[:1]
    serializer_class = Dht1DataSerializer


class Dht1HistoryViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides `list`, `create`, `retrieve`, `update` and `destroy` actions.
    """
    queryset = Dht1History.objects.all().order_by('-id')
    serializer_class = Dht1HistorySerializer


class Dht2ViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides `list`, `create`, `retrieve`, `update` and `destroy` actions.
    """
    queryset = Dht2Data.objects.all().order_by('-id')
    serializer_class = Dht2DataSerializer


class Dht2LastViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides `list`, `create`, `retrieve`, `update` and `destroy` actions.
    """
    queryset = Dht2Data.objects.all().order_by('-id')[:1]
    serializer_class = Dht2DataSerializer


class Dht2HistoryViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides `list`, `create`, `retrieve`, `update` and `destroy` actions.
    """
    queryset = Dht2History.objects.all().order_by('-id')
    serializer_class = Dht2HistorySerializer
