import { getFields, getDivs, getGaugePlotly, getHystoryPlotly, getDataForLineChart } from './modules/plotlyData.js'

const pathname = document.location.pathname.slice(1, -1);
const fields = getFields(pathname);

/* Box block & gauge block */
function updateSensorReadings() {
  fetch(`/api/${pathname}-last/`)
    .then((response) => response.json())
    .then((jsonResponse) => {
      const res = jsonResponse.results[0]

      const localDate = new Date(res.full_date).toLocaleString('ru');
      const dateEl = document.querySelector('#local-date')
      dateEl.innerHTML = localDate;

      fields.forEach((field) => {
        const fieldData = res[field]
        updateGauge(field, fieldData)
        updateBoxes(field, fieldData)
      })
    });
};

function updateGauge(field, fieldData) {
  const data_update = {
    value: fieldData,
  };
  Plotly.update(document.querySelector(`#${field}-gauge`), data_update);
};

function updateBoxes(field, fieldData) {
  const div = document.querySelector(`#${field}`);
  div.innerHTML = fieldData;
};

/* Line chart block */
function updateLastData() {
  let datesArr;
  fetch(`/api/${pathname}/`)
    .then((res) => res.json())
    .then((jsonRes) => {
      const res = jsonRes.results
      datesArr = getDataForLineChart(res, 'full_date');

      fields.forEach((field) => {
        const fieldData = getDataForLineChart(res, field);
        updateCharts(
          datesArr,
          fieldData,
          document.querySelector(`#${field}-chart`)
        )
      })
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

function init() {
  getGaugePlotly(fields, getDivs('.gauge__data'));
  getHystoryPlotly(fields, getDivs('.charts__chart'));
  updateSensorReadings();
  updateLastData();
  loop();
};

window.onload = (e) => {
  init();
};