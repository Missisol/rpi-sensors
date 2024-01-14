import { 
  timer, 
  getFields, 
} from './modules/commonData.js'

function init() {
  const links = document.querySelectorAll('.home__link');
  initBoxes(links);
}

function initBoxes(links) {
  links.forEach((node) => {
    const pathname = node.id
    const fields = getFields(pathname);
    updateSensorReadings(fields, pathname);
    loop(fields, pathname);
  })
}

function loop(fields, pathname) {
  setTimeout(() => {
    updateSensorReadings(fields, pathname);
    loop(fields, pathname);
  }, timer);
}

function updateSensorReadings(fields, pathname) {
  fetch(`/api/${pathname}-last/`)
    .then((response) => response.json())
    .then((jsonResponse) => {
      const res = jsonResponse.results[0]

      const localDate = new Date(res.full_date).toLocaleString('ru');
      const dateEl = document.querySelector(`#${pathname}-date`);
      dateEl.innerHTML = localDate;

      fields.forEach((field) => {
        const fieldData = res[field]
        updateBoxes(field, fieldData, pathname)
      })
    });
}

function updateBoxes(field, fieldData, pathname) {
  const div = document.querySelector(`#${pathname}-${field}`);
  div.innerHTML = fieldData;
}

init();
