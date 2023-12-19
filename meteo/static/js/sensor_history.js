import { getProcessedFields, getDeltaPlotly } from './modules/plotlyHistory.js';
import { timer, getDataForLineChart, getDivs } from './modules/commonData.js';

const pathname = document.location.pathname.replaceAll('/', '');
const fields = getProcessedFields(pathname);
let bgcolor;

function updateDelta() {
  fetch(`/api/${pathname}/`)
    .then((res) => res.json())
    .then((jsonRes) => {
      const res = jsonRes.results;
      const datesArr = getDataForLineChart(res, 'date');

      for (const [key, value] of  Object.entries(fields)) {
        const y = []
        value.forEach((val) => {
          y.push(getDataForLineChart(res, val));
        })
        Plotly.update(
          document.querySelector(`#${key}-chart`),
          {
            x: [datesArr],
            y,
          },
        )
      };
  })
}

function changeBgcolor() {
  window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', event => {
    bgcolor = event.matches ? '#191919' : '#fff';

    const layout_update = {
      paper_bgcolor: bgcolor,
      plot_bgcolor: bgcolor,
    }
    
    for (const [key, value] of  Object.entries(fields)) {
      Plotly.update(document.querySelector(`#${key}-chart`), {}, layout_update);
    }
  })
}


function loop() {
  setTimeout(() => {
    updateDelta();
    loop();
  }, timer);
}

function init() {
  getDeltaPlotly(Object.keys(fields), getDivs('.charts__chart'));
  updateDelta();
  loop();
  changeBgcolor();
}

window.onload = (e) => {
  init();
}