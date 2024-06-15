const mediaQuery = window.matchMedia('(prefers-color-scheme: dark)');

const timer = 30000;
// const timer = 60 * 1000 * 5
// const timer = 60 * 1000 * 15 // every 15 minutes

const config = {
  responsive: true,
  displayModeBar: false,
};

const dataFields = ['temperature', 'humidity', 'pressure'];

const lineChartDataArr = [
  { name: 'temperature', legend: 'температура', text: 'Температура', color: '#3ba639' },
  { name: 'humidity', legend: 'влажность', text: 'Влажность', color: '#047df3' },
  { name: 'pressure', legend: 'давление', text: 'Давление', color: '#CC66FF' },
];

const getFields = (str) => {
  return str.includes('bme') ? dataFields : dataFields.slice(0, -1);
};

const getDataForLineChart = (dataArr, field) => {
  return dataArr.map(item => Intl.DateTimeFormat('ru_RU', {minute: '2-digit', hour: '2-digit'}).format(new Date(item[field])))
};

const getFilteredDataArr = (fields, arr) => {
  return arr.filter((data) => fields.some((el) => data.name === el))
};

const getDivs = (selector) => {
  const divs = [];
  const nodeEls = document.querySelectorAll(selector);
  nodeEls.forEach((el) => divs.push(el));
  return divs;
};

const getColors = (condition1, condition2) => {
  let bgcolor, titlecolor;

  if (condition1) {
    bgcolor = condition2 === 'dark' ? '#191919' : '#fff';
    titlecolor = condition2 === 'dark' ? '#cecece' : '#595959';
  } else {
    bgcolor = mediaQuery.matches ? '#191919' : '#fff';
    titlecolor = mediaQuery.matches ? '#cecece' : '#595959';
  }

  return { bgcolor, titlecolor }
}

const setListeners = (changeBgcolor) => {
  const themeSwitchers = document.querySelectorAll('.theme-switch');

  [...themeSwitchers].forEach((radio) => {
    radio.addEventListener('change', (event) => {
      const condition1 = event?.target?.value !== 'auto'
      const { bgcolor, titlecolor } = getColors(condition1, event.target.value);
      changeBgcolor(bgcolor, titlecolor);
    })
  });

  mediaQuery.addEventListener('change', () => {
    const modeOverride = localStorage.getItem('color-mode')
    const { bgcolor, titlecolor } = getColors(modeOverride, modeOverride);
    changeBgcolor(bgcolor, titlecolor);
  });
}


export { 
  timer, 
  config, 
  lineChartDataArr, 
  getFields, 
  getDataForLineChart, 
  getFilteredDataArr, 
  getDivs, 
  getColors,
  setListeners,
};