box1 = [
    {
        'dataName': "Температура, &deg;C",
        'className': 'sensor-icon--temperature',
        'id': 'temperature',
    }, 
    {
        'dataName': "Влажность, %", 
        'className': 'sensor-icon--humidity',
        'id': 'humidity',
    }, 
]

box2 = [
     {
        'dataName': "Давление, мм.рт.ст.", 
        'className': 'sensor-icon--pressure',
        'id': 'pressure',
    },
]

box3 = [*box1, *box2]

gauge1 = [
    'temperature',
    'humidity',
]

gauge2 = ['pressure']

gauge3 = [*gauge1, *gauge2]

data_list =  [
    { 
        'box': box1,
    },
    {
        'gauge': gauge1,
    },
]


bme_data_list =  [
    { 
        'box': box3,
    },
    {
        'gauge': gauge3,
    },
]
