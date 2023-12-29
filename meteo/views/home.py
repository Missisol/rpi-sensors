from django.http import HttpResponse
from django.shortcuts import render

from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
  template_name = 'meteo/home.html'

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context["greeting"] = 'Hello'
      return context
