from django.http import HttpResponse


def bme_data(request):
    return HttpResponse("Hello, world. You're at the polls index." )