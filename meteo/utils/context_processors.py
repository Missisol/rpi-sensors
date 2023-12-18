def get_menu(request):
  return {
    'menu': [
    ['bme', '/bme/', 'Данные BME280'],
    ['bme-history', '/bme-history/', 'История BME280'],
    ['dht1', '/dht1/', 'Данные DHT22-1'], 
    ['dht1-history', '/dht1-history/', 'История DHT22-1'], 
    ['dht2', '/dht2/', 'Данные DHT22-2'], 
    ['dht2-history', '/dht2-history/', 'История DHT22-2'], 
    ]
  }