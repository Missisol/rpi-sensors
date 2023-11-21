import { getProcessedFields, getDeltaPlotly } from './modules/plotlyHistory.js';
import { timer, getDataForLineChart, getDivs } from './modules/commonData.js';

const pathname = document.location.pathname.slice(1, 4);
const fields = getProcessedFields(pathname);

function updateDelta() {
  fetch(`/api/${pathname}-history/`)
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
};

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
};

window.onload = (e) => {
  init();
};