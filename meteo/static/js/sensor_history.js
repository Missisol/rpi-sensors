import { getProcessedFields, getDeltaPlotly } from './modules/plotlyHistory.js';
import { 
  timer, 
  getDataForLineChart, 
  getDivs, 
  setListeners, 
} from './modules/commonData.js';

const pathname = document.location.pathname.replaceAll('/', '');
const fields = getProcessedFields(pathname);

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

function changeBgcolor(bgcolor, titlecolor) {
  const layout_update = {
    paper_bgcolor: bgcolor,
    plot_bgcolor: bgcolor,
    font: {
      color: titlecolor,
    },
  }
  
  for (const [key, value] of Object.entries(fields)) {
    Plotly.update(document.querySelector(`#${key}-chart`), {}, layout_update);
  }
}

function loop() {
  setTimeout(() => {
    updateDelta();
    loop();
  }, timer);
}

function init() {
  setListeners(changeBgcolor);
  getDeltaPlotly(Object.keys(fields), getDivs('.charts__chart'));
  updateDelta();
  loop();
}

init();
