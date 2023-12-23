import { getGaugePlotly, getHystoryPlotly } from './modules/plotlyData.js'
import { 
  timer, 
  getDataForLineChart, 
  getDivs, 
  getFields, 
  setListeners, 
} from './modules/commonData.js'

const pathname = document.location.pathname.replaceAll('/', '');
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
}

function updateGauge(field, fieldData) {
  const data_update = {
    value: fieldData,
  };
  Plotly.update(document.querySelector(`#${field}-gauge`), data_update);
}

function updateBoxes(field, fieldData) {
  const div = document.querySelector(`#${field}`);
  div.innerHTML = fieldData;
}

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
}

function updateCharts(xArray, yArray, historyDiv) {
  const data_update = {
    x: [xArray],
    y: [yArray],
  };
  Plotly.update(historyDiv, data_update);
}

function changeBgcolor(bgcolor, titlecolor) {
  const layout_update = {
    paper_bgcolor: bgcolor,
    plot_bgcolor: bgcolor,
    font: {
      color: titlecolor,
    },
  }

  fields.map((field) => {
    Plotly.update(document.querySelector(`#${field}-chart`), {}, layout_update);
    Plotly.update(document.querySelector(`#${field}-gauge`), {}, layout_update);
  })
}

function loop() {
  setTimeout(() => {
    updateSensorReadings();
    updateLastData();
    loop();
  }, timer);
}

function init() {
  setListeners(changeBgcolor);
  getGaugePlotly(fields, getDivs('.gauge__data'));
  getHystoryPlotly(fields, getDivs('.charts__chart'));
  updateSensorReadings();
  updateLastData();
  loop();
}

init();
