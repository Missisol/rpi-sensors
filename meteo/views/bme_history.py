from django.http import HttpResponse
from django.shortcuts import render

from django.views.generic import ListView

from meteo.models import BmeHistory

class BmeHistoryListView(ListView):
    model = BmeHistory


