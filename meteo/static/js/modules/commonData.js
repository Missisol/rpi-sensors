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
  { name: 'pressure', legend: 'давление', text: 'Давление', color: '#3d3c3c'},
];

function getFields(str) {
  return str === 'bme' ? dataFields : dataFields.slice(0, -1);
};

function getDataForLineChart(dataArr, field) {
  return dataArr.map(item => item[field])
};

const getFilteredDataArr = (fields, arr) => {
  return arr.filter((data) => fields.some((el) => data.name === el ))
};

function getDivs(selector) {
  const divs = [];
  const nodeEls = document.querySelectorAll(selector);
  nodeEls.forEach((el) => divs.push(el));
  return divs;
};

export { timer, config, lineChartDataArr, getFields, getDataForLineChart, getFilteredDataArr, getDivs };