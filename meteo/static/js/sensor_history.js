import { getProcessedFields, getDeltaPlotly } from './modules/plotlyHistory.js';
import { timer, getDataForLineChart, getDivs } from './modules/commonData.js';

const pathname = document.location.pathname.replaceAll('/', '');
const fields = getProcessedFields(pathname);
const themeSwitchers = document.querySelectorAll('.theme-switch');
const mediaQuery = window.matchMedia('(prefers-color-scheme: dark)');
let bgcolor, titlecolor;

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

mediaQuery.addEventListener('change', () => {
  const modeOverride = localStorage.getItem('color-mode')
  if (modeOverride) {
    bgcolor = modeOverride === 'dark' ? '#191919' : '#fff';
    titlecolor = modeOverride === 'dark' ? '#cecece' : '#595959';
  } else {
    bgcolor = mediaQuery.matches ? '#191919' : '#fff';
    titlecolor = mediaQuery.matches ? '#cecece' : '#595959';
  }
  changeBgcolor();
});

[...themeSwitchers].forEach((radio) => {
  radio.addEventListener('change', (event) => {
    if (event?.target?.value !== 'auto') {
      bgcolor = event.target.value === 'dark' ? '#191919' : '#fff';
      titlecolor = event.target.value === 'dark' ? '#cecece' : '#595959';
    } else {
      bgcolor = mediaQuery.matches ? '#191919' : '#fff';
      titlecolor = mediaQuery.matches ? '#cecece' : '#595959';
    }
    changeBgcolor();
  })
});

function changeBgcolor() {
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
  getDeltaPlotly(Object.keys(fields), getDivs('.charts__chart'));
  updateDelta();
  loop();
}

window.addEventListener('load', () => {
  init();
})
