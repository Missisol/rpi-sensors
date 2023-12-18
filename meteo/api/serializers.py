from rest_framework import serializers

from meteo.models import BmeData, BmeHistory, Dht1Data, Dht1History, Dht2Data, Dht2History


class BmeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BmeData
        fields = ['id', 'temperature', 'humidity', 'pressure', 'full_date', 'date']


class BmeHistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BmeHistory
        fields = ['id', 'min_temperature', 'max_temperature', 'min_humidity', 'max_humidity', 'min_pressure', 'max_pressure', 'date']


class Dht1DataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dht1Data
        fields = ['id', 'temperature', 'humidity', 'full_date', 'date']


class Dht1HistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dht1History
        fields = ['id', 'min_temperature', 'max_temperature', 'min_humidity', 'max_humidity', 'date']


class Dht2DataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dht2Data
        fields = ['id', 'temperature', 'humidity', 'full_date', 'date']


class Dht2HistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dht2History
        fields = ['id', 'min_temperature', 'max_temperature', 'min_humidity', 'max_humidity', 'date']


