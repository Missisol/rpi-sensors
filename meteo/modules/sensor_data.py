bme_data_list =  [
           { 
                'box': [
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
                    {
                        'dataName': "Давление, мм.рт.ст.", 
                        'className': 'bx bxs-tachometer readings readings--three',
                        'id': 'pressure',
                    },
                ]
            },
            {
                'gauge': [
                    'temperature',
                    'humidity',
                    'pressure',
                ]
            }
        ]

dht_data_list =  [
           { 
                'box': [
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
            },
            {
                'gauge': [
                    'temperature',
                    'humidity',
                ]
            }
        ]