from rest_framework import serializers

from meteo.models import BmeData, BmeHistory, DhtData, DhtHistory


class BmeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BmeData
        fields = ['id', 'temperature', 'humidity', 'pressure', 'full_date', 'date']


class BmeHistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BmeHistory
        fields = ['id', 'min_temperature', 'max_temperature', 'min_humidity', 'max_humidity', 'min_pressure', 'max_pressure', 'date']


class DhtDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DhtData
        fields = ['id', 'temperature', 'humidity', 'date']


class DhtHistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DhtHistory
        fields = ['id', 'min_temperature', 'max_temperature', 'min_humidity', 'max_humidity', 'date']


