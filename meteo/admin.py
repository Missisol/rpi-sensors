from django.contrib import admin

# from meteo import models
from meteo.models import BmeData, BmeHistory, Dht1Data, Dht2Data, Dht1History, Dht2History


@admin.register(BmeData)
class BmeDataAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Дата', {
        'fields': [
            'date', 
            'full_date',
        ]
        }),
        ('Данные bme280', {
        'fields': [
            'temperature', 
            'humidity', 
            'pressure',
            ]
        })
    ]
    list_display = [
        'id', 
        'date', 
        'temperature', 
        'humidity', 
        'pressure',
        "full_date",
    ]
    list_filter = ['date', 'full_date']


@admin.register(BmeHistory)
class BmeHistoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['date']}),
        ('История bme280', {
        'fields': [
            'min_temperature', 
            'max_temperature', 
            'min_humidity', 
            'max_humidity', 
            'min_pressure', 
            'max_pressure',
            ]
        })
    ]
    list_display = [
        'id', 
        'date', 
        'min_temperature', 
        'max_temperature', 
        'min_humidity', 
        'max_humidity', 
        'min_pressure', 
        'max_pressure',
    ]
    

@admin.register(Dht1Data)
class Dht1DataAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Дата', {'fields': ['date']}),
        ('Данные ВРЕ22', {
        'fields': [
            'temperature', 
            'humidity', 
            ]
        })
    ]
    list_display = [
        'id', 
        'date', 
        'temperature', 
        'humidity', 
        'full_date',
    ]


@admin.register(Dht1History)
class Dht1HistoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['date']}),
        ('История dht22', {
        'fields': [
            'min_temperature', 
            'max_temperature', 
            'min_humidity', 
            'max_humidity', 
            ]
        })
    ]
    list_display = [
        'id', 
        'date', 
        'min_temperature', 
        'max_temperature', 
        'min_humidity', 
        'max_humidity', 
    ]


@admin.register(Dht2Data)
class Dht2DataAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Дата', {'fields': ['date']}),
        ('Данные ВРЕ22', {
        'fields': [
            'temperature', 
            'humidity', 
            ]
        })
    ]
    list_display = [
        'id', 
        'date', 
        'temperature', 
        'humidity', 
        'full_date',
    ]


@admin.register(Dht2History)
class Dht2HistoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['date']}),
        ('История dht22', {
        'fields': [
            'min_temperature', 
            'max_temperature', 
            'min_humidity', 
            'max_humidity', 
            ]
        })
    ]
    list_display = [
        'id', 
        'date', 
        'min_temperature', 
        'max_temperature', 
        'min_humidity', 
        'max_humidity', 
    ]

