box1 = [
    {
        'dataName': "Температура, &deg;C",
        'className': 'bx bxs-thermometer readings',
        'id': 'temperature',
    }, 
    {
        'dataName': "Влажность, %", 
        'className': 'bx bxs-droplet-half readings readings--two',
        'id': 'humidity',
    }, 
]

box2 = [
     {
        'dataName': "Давление, мм.рт.ст.", 
        'className': 'bx bxs-tachometer readings readings--three',
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
