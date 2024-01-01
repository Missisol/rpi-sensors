def get_menu(request):
  return {
    'menu': [
    ['bme', '/bme/', 'Данные BME280', 'Данные датчика BME280'],
    ['bme-history', '/bme-history/', 'История BME280', 'Минимальные и максимальные значения BME280'],
    ['dht1', '/dht1/', 'Данные DHT22-1', 'Данные датчика DHT22-1'], 
    ['dht1-history', '/dht1-history/', 'История DHT22-1', 'Минимальные и максимальные значения DHT22-1'], 
    ['dht2', '/dht2/', 'Данные DHT22-2', 'Данные датчика DHT22-2'], 
    ['dht2-history', '/dht2-history/', 'История DHT22-2', 'Минимальные и максимальные значения DHT22-2'], 
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