const dateEl = document.querySelector('#local-date')

const temperatureDiv = document.getElementById("temperature");
const humidityDiv = document.getElementById("humidity");
const pressureDiv = document.getElementById("pressure");

const temperatureGaugeDiv = document.getElementById("temperature-gauge");
const humidityGaugeDiv = document.getElementById("humidity-gauge");
const pressureGaugeDiv = document.getElementById("pressure-gauge");
const gaugeDivs = [temperatureGaugeDiv, humidityGaugeDiv, pressureGaugeDiv] 

const gaugeDataArr = [
  { 
    name: 'temperature', 
    text: 'Температура, &deg;C',
    reference: 30,
    range: [null, 50],
    color: "#3ba639",
    steps: [
      { range: [0, 20], color: "#fff" },
      { range: [20, 30], color: "#aaffa9" },
      { range: [30, 50], color: "#ef7985" },
    ],
    value: 40,
  },
  { 
    name: 'humidity', 
    text: 'Влажность, %', 
    reference: 40,
    range: [null, 100],
    color: "#047df3",
    steps: [
      { range: [0, 40], color: "#fff" },
      { range: [40, 60], color: "#a6cdf3" },
      { range: [60, 100], color: "#70b0ef" },
    ],
    value: 70,
  },
  { 
    name: 'pressure', 
    text: 'Давление, мм.рт.ст.', 
    reference: 748,
    range: [700, 800],
    color: "#808080",
    steps: [
      { range: [700, 748], color: "#fff" },
      { range: [748, 800], color: "#cecece" },
    ],
    value: 760,
  },
];

// gauge layout
const layout = { 
  width: 300,
  height: 250, 
  margin: { t: 30, b: 30, l: 30, r: 30 },
};

const config = {
  responsive: true,
  displayModeBar: false,
};

function getGaugePlotly() {
  gaugeDataArr.forEach((data, idx) => {
    const trace = [
      {
        type: "indicator",
        mode: "gauge+number",
        title: { text: data.text },
        gauge: {
          axis: { range: data.range },
          bar: { color: data.color},
          steps: data.steps,
          threshold: {
            line: { color: "red", width: 4 },
            thickness: 0.75,
            value: data.value,
          },
        },
      },
    ];
    Plotly.newPlot(gaugeDivs[idx], trace, layout, {displayModeBar: false});
  })
};

function updateSensorReadings() {
  fetch(`/api/bme-last/`)
    .then((response) => response.json())
    .then((jsonResponse) => {
      const res = jsonResponse.results[0]
      const temperature = res.temperature;
      const humidity = res.humidity;
      const pressure = res.pressure;

      updateGauge(temperature, humidity, pressure);
    });
};

function updateGauge(temperature, humidity, pressure) {
  const temperature_update = {
    value: temperature,
  };
  const humidity_update = {
    value: humidity,
  };
  const pressure_update = {
    value: pressure,
  };

  Plotly.update(temperatureGaugeDiv, temperature_update);
  Plotly.update(humidityGaugeDiv, humidity_update);
  Plotly.update(pressureGaugeDiv, pressure_update);
}

const timer = 30000
// const timer = 60 * 1000 * 5
// const timer = 60 * 1000 * 15 // every 15 minutes

function loop() {
  setTimeout(() => {
    updateSensorReadings();
    loop();
  }, timer);
}

(function init() {
  getGaugePlotly();
  updateSensorReadings();
  loop();
})();