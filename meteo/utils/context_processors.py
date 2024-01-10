def get_dashboard(request):
  return {
    'menu': [
    ['bme', 'Данные BME280'],
    ['dht1', 'Данные DHT22-1'], 
    ['dht2', 'Данные DHT22-2'], 
    ]
  }

def get_nested_menu(request):
  return {
    'nested_menu': [
      ['Данные', [
        ['bme', '/bme/', 'BME280',],
        ['dht1', '/dht1/', 'DHT22-1',], 
        ['dht2', '/dht2/', 'DHT22-2',], 
      ]],
      ['История', [
        ['bme-history', '/bme-history/', 'BME280',],
        ['dht1-history', '/dht1-history/', 'DHT22-1',], 
        ['dht2-history', '/dht2-history/', 'DHT22-2',], 
      ]],
    ]
  }