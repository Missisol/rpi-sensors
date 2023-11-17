const temperatureDeltaEl = document.querySelector('#temperature-delta')
const humidityDeltaEl = document.querySelector('#humidity-delta')
const deltaDivs = [temperatureDeltaEl, humidityDeltaEl]

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

const deltaDataArr = [
  { name: 'температура', text: 'Температура', color: '#3ba639' },
  { name: 'влажность', text: 'Влажность', color: '#047df3' },
];


function getDeltaPlotly() {
  deltaDataArr.forEach((data, idx) => {
    const trace1 = {
      x: [],
      y: [],
      name: `min ${data.name}`,
      mode: "lines+markers",
      line: {
        dash: 'dot'
      },
    };
    const trace2 = {
      x: [],
      y: [],
      name: `max ${data.name}`,
      mode: "lines+markers",
      line: {},
    };
    const traces = [trace1, trace2];
    const layout = {
      height: 300,
      title: {
        text: data.text
      },
      font: {
        size: 14,
        color: "#808080",
      },
      legend: {
        x: 0,
        y: -1.5,
      }
    };
  
    Plotly.newPlot(deltaDivs[idx], traces, layout, config)
  })
};

function getDataForLineChart(dataArr, field) {
  return dataArr.map(item => item[field])
};

function updateDelta() {
  let datesArr;
  let minTempArr;
  let maxTempArr;
  let minHumArr;
  let maxHumArr;

  fetch('/api/dht-history/')
    .then((res) => res.json())
    .then((jsonRes) => {
      const res = jsonRes.results;
      datesArr = getDataForLineChart(res, 'date');
      minTempArr = getDataForLineChart(res, 'min_temperature');
      maxTempArr = getDataForLineChart(res, 'max_temperature');
      minHumArr = getDataForLineChart(res, 'min_humidity');
      maxHumArr = getDataForLineChart(res, 'max_humidity');

    Plotly.update(
      temperatureDeltaEl, 
     {
        x: [datesArr],
        y: [minTempArr, maxTempArr],
      },
      {colorway: ['#3ba639']}
    );
    Plotly.update(
      humidityDeltaEl, 
      {
        x: [datesArr],
        y: [minHumArr, maxHumArr],
      },
      {colorway: ['#047df3']}
    );
  })
}

const timer = 30000
// const timer = 60 * 1000 * 5
// const timer = 60 * 1000 * 15 // every 15 minutes

function loop() {
  setTimeout(() => {
    updateDelta();
    loop();
  }, timer);
}

(function init() {
  getDeltaPlotly();
  updateDelta();
  loop();
})();