const dateEl = document.querySelector('#local-date')

const temperatureDiv = document.getElementById("temperature");
const humidityDiv = document.getElementById("humidity");

const temperatureGaugeDiv = document.getElementById("temperature-gauge");
const humidityGaugeDiv = document.getElementById("humidity-gauge");
const gaugeDivs = [temperatureGaugeDiv, humidityGaugeDiv] 

const temperatureHistoryDiv = document.getElementById("temperature-chart");
const humidityHistoryDiv = document.getElementById("humidity-chart");
const historyDivs = [temperatureHistoryDiv, humidityHistoryDiv]

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
];

/* Gauge layout */
const layout = { 
  width: 300,
  height: 250, 
  margin: { t: 30, b: 30, l: 30, r: 30 },
};

/* Gauge config */
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
    Plotly.newPlot(gaugeDivs[idx], trace, layout, config);
  })
};

function updateSensorReadings() {
  fetch(`/api/dht-last/`)
    .then((response) => response.json())
    .then((jsonResponse) => {
      const res = jsonResponse.results[0]
      const temperature = res.temperature;
      const humidity = res.humidity;
      const localDate = new Date(res.full_date).toLocaleString('ru');

      updateGauge(temperature, humidity);
      updateBoxes(temperature, humidity, localDate);
    });
};

function updateGauge(temperature, humidity) {
  const temperature_update = {
    value: temperature,
  };
  const humidity_update = {
    value: humidity,
  };

  Plotly.update(temperatureGaugeDiv, temperature_update);
  Plotly.update(humidityGaugeDiv, humidity_update);
}

function updateBoxes(temperature, humidity, localDate) {
  temperatureDiv.innerHTML = temperature;
  humidityDiv.innerHTML = humidity;
  dateEl.innerHTML = localDate;
}

const historyDataArr = [
  { name: 'temperature', text: 'Температура', colorway: '3ba639' },
  { name: 'humidity', text: 'Влажность', colorway: '047df3' },
];

function getHystoryPlotly() {
  historyDataArr.forEach((data, idx) => {
    const trace = {
      x: [],
      y: [],
      name: data.name,
      mode: "lines+markers",
      type: "line",
    };
    const layout = {
      height: 300,
      title: {
        text: data.text,
      },
      font: {
        size: 14,
        color: "#808080",
      },
      colorway: [data.colorway],
    };
    Plotly.newPlot(historyDivs[idx], [trace], layout, config);
  })
};

function getDataForLineChart(dataArr, field) {
  return dataArr.map(item => item[field])
};

function updateLastData() {
  let datesArr;
  let temperatureArr;
  let humidityArr;
  fetch('/api/dht/')
    .then((res) => res.json())
    .then((jsonRes) => {
      const res = jsonRes.results
      datesArr = getDataForLineChart(res, 'full_date');
      temperatureArr = getDataForLineChart(res, 'temperature');
      humidityArr = getDataForLineChart(res, 'humidity');

      updateCharts(
        datesArr,
        temperatureArr,
        temperatureHistoryDiv,
      );
      updateCharts(
        datesArr,
        humidityArr,
        humidityHistoryDiv,
      );
  })
};

function updateCharts(xArray, yArray, historyDiv) {
  const data_update = {
    x: [xArray],
    y: [yArray],
  };
    Plotly.update(historyDiv, data_update);
}

const timer = 30000
// const timer = 60 * 1000 * 5
// const timer = 60 * 1000 * 15 // every 15 minutes

function loop() {
  setTimeout(() => {
    updateSensorReadings();
    updateLastData();
    loop();
  }, timer);
}

(function init() {
  getGaugePlotly();
  updateSensorReadings();
  getHystoryPlotly();
  updateLastData();
  loop();
})();