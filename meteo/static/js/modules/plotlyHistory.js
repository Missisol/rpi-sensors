const bmeFields = {
  temperature: ['min_temperature', 'max_temperature'],
  humidity: ['min_humidity', 'max_humidity'],
  pressure: ['min_pressure', 'max_pressure'],
};

const dhtFields = {
  temperature: ['min_temperature', 'max_temperature'],
  humidity: ['min_humidity', 'max_humidity'],
};

const config = {
  responsive: true,
  displayModeBar: false,
};

const colorway = {
  temperature: '#3ba639', 
  humidity: '#047df3',
  pressure: '#3d3c3c',
};

const getFields = (str) => {
  return str === 'bme' ? bmeFields : dhtFields;
};

const deltaDataArr = [
  { name: 'temperature', legend: 'температура', text: 'Температура', color: '#3ba639' },
  { name: 'humidity', legend: 'влажность', text: 'Влажность', color: '#047df3' },
  { name: 'pressure', legend: 'давление', text: 'Давление', color: '#3d3c3c'},
];

const getDataArr = (fields) => {
  return deltaDataArr.filter((data) => fields.some((el) => data.name === el ))
};

function getDeltaPlotly(fields, divs) {
  const dataArr = getDataArr(fields)
  dataArr.forEach((data, idx) => {
    const trace1 = {
      x: [],
      y: [],
      name: `min ${data.legend}`,
      mode: "lines+markers",
      line: {
        dash: 'dot'
      },
    };
    const trace2 = {
      x: [],
      y: [],
      name: `max ${data.legend}`,
      mode: "lines+markers",
      line: {},
    };
    const traces = [trace1, trace2];
    const layout = {
      height: 300,
      title: {
        text: data.text
      },
      font: {
        size: 14,
        color: "#808080",
      },
      legend: {
        x: 0,
        y: -1,
      }
    };
  
    Plotly.newPlot(divs[idx], traces, layout, config);
  });
};

function getDataForLineChart(dataArr, field) {
  return dataArr.map(item => item[field])
};

function getDivs(selector) {
  const divs = [];
  const nodeEls = document.querySelectorAll(selector);
  nodeEls.forEach((el) => divs.push(el));
  return divs;
};

export { colorway, getFields, getDeltaPlotly, getDataForLineChart, getDivs }