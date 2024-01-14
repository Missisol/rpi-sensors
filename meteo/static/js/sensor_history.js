import { getProcessedFields, getDeltaPlotly } from './modules/plotlyHistory.js';
import {
  timer,
  getDataForLineChart,
  getDivs,
  setListeners,
} from './modules/commonData.js';
import { minDate, getFormettedDate } from './modules/helpers.js';

const pathname = document.location.pathname.replaceAll('/', '');
const fields = getProcessedFields(pathname);
let params = '';
let error = '';

function updateDelta() {
  fetch(`/api/${pathname}/?${params}`)
    .then((res) => res.json())
    .then((jsonRes) => {
      const res = jsonRes.results;
      const datesArr = getDataForLineChart(res, 'date');

      for (const [key, value] of Object.entries(fields)) {
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

const setupDatePicker = () => {
  const startInput = document.querySelector('#start-date');
  const endInput = document.querySelector('#end-date');
  const formattedDate = getFormettedDate();

  startInput.setAttribute('min', minDate);
  startInput.setAttribute('max', formattedDate);
  endInput.setAttribute('min', minDate);
  endInput.setAttribute('max', formattedDate);
}

const validateForm = (start, end) => {
  error = start > end ? 'Начало периода позже конца периода.' : ''
  updateErrorSpan();
}

function updateErrorSpan() {
  const errorEl = document.querySelector('#form-error');
  errorEl.innerHTML = error;
}

function setupForm() {
  setupDatePicker();

  const buttonResetEl = document.querySelector('#button-reset');
  buttonResetEl.addEventListener('click', () => {
    params = '';
    error = '';
    updateErrorSpan();
    updateDelta();
  });
}

function initForm() {
  const formEl = document.querySelector('#history-form');
  formEl.addEventListener('submit', (e) => {
    e.preventDefault();

    validateForm(formEl.start_date.value, formEl.end_date.value);

    if (!error) {
      params = `start_date=${formEl.start_date.value}&end_date=${formEl.end_date.value}&limit=2000`;
      updateDelta();
    }
  });
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
  initForm();
  setupForm();
  loop();
}

init();
