from django.views.generic.base import TemplateView
from meteo.utils.sensor_data import box4, box5


class HomePageView(TemplateView):
  template_name = 'meteo/home.html'

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context["bme_list"] = box5
      context["dht_list"] = box4
      return context
