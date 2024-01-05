from rest_framework import viewsets

from meteo.models import BmeData, BmeHistory, Dht1Data, Dht1History, Dht2Data, Dht2History
from .serializers import BmeSerializer, BmeHistorySerializer, Dht1DataSerializer, Dht1HistorySerializer, Dht2DataSerializer, Dht2HistorySerializer


class BmeViewSet(viewsets.ModelViewSet):
    queryset = BmeData.objects.all().order_by('-id')
    serializer_class = BmeSerializer


class BmeLastViewSet(viewsets.ModelViewSet):
    queryset = BmeData.objects.all().order_by('-id')[:1]
    serializer_class = BmeSerializer


class BmeHistoryViewSet(viewsets.ModelViewSet):
    queryset = BmeHistory.objects.all().order_by('-id')
    serializer_class = BmeHistorySerializer

    def get_queryset(self):
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        if start_date and end_date:   
            queryset = self.queryset.filter(date__range=(start_date, end_date))
            return queryset
        else: 
            return self.queryset


class Dht1ViewSet(viewsets.ModelViewSet):
    queryset = Dht1Data.objects.all().order_by('-id')
    serializer_class = Dht1DataSerializer


class Dht1LastViewSet(viewsets.ModelViewSet):
    queryset = Dht1Data.objects.all().order_by('-id')[:1]
    serializer_class = Dht1DataSerializer


class Dht1HistoryViewSet(viewsets.ModelViewSet):
    queryset = Dht1History.objects.all().order_by('-id')
    serializer_class = Dht1HistorySerializer

    def get_queryset(self):
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        if start_date and end_date:   
            queryset = self.queryset.filter(date__range=(start_date, end_date))
            return queryset
        else: 
            return self.queryset


class Dht2ViewSet(viewsets.ModelViewSet):
    queryset = Dht2Data.objects.all().order_by('-id')
    serializer_class = Dht2DataSerializer


class Dht2LastViewSet(viewsets.ModelViewSet):
    queryset = Dht2Data.objects.all().order_by('-id')[:1]
    serializer_class = Dht2DataSerializer


class Dht2HistoryViewSet(viewsets.ModelViewSet):
    queryset = Dht2History.objects.all().order_by('-id')
    serializer_class = Dht2HistorySerializer

    def get_queryset(self):
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        if start_date and end_date:   
            queryset = self.queryset.filter(date__range=(start_date, end_date))
            return queryset
        else: 
            return self.queryset
