const bmeFields = ['temperature', 'humidity', 'pressure']
const dhtFields = ['temperature', 'humidity']

const getFields = (str) => {
  return str === 'bme' ? bmeFields : dhtFields;
};

const config = {
  responsive: true,
  displayModeBar: false,
};

/* Gauge layout */
const layout = { 
  width: 300,
  height: 250, 
  margin: { t: 30, b: 30, l: 30, r: 30 },
};

const gaugeDataArr = [
  { 
    name: 'temperature', 
    text: 'Температура, &deg;C',
    reference: 30,
    range: [null, 50],
    color: "#3ba639",
    steps: [
      { range: [0, 20], color: "#fff" },
      { range: [20, 30], color: "#aaffa9" },
      { range: [30, 50], color: "#ef7985" },
    ],
    value: 40,
  },
  { 
    name: 'humidity', 
    text: 'Влажность, %', 
    reference: 40,
    range: [null, 100],
    color: "#047df3",
    steps: [
      { range: [0, 40], color: "#fff" },
      { range: [40, 60], color: "#a6cdf3" },
      { range: [60, 100], color: "#70b0ef" },
    ],
    value: 70,
  },
  { 
    name: 'pressure', 
    text: 'Давление, мм.рт.ст.', 
    reference: 748,
    range: [700, 800],
    color: "#808080",
    steps: [
      { range: [700, 748], color: "#fff" },
      { range: [748, 800], color: "#cecece" },
    ],
    value: 760,
  },
];

const historyDataArr = [
  { name: 'temperature', text: 'Температура', colorway: '3ba639' },
  { name: 'humidity', text: 'Влажность', colorway: '047df3' },
  { name: 'pressure', text: 'Давление', colorway: '595959'},
];

function getDataArr(fields, plotArrName) {
  const dataArr = plotArrName === 'gaugeDataArr'
    ?  gaugeDataArr 
    :  historyDataArr

  return dataArr.filter((data) => fields.some((el) => data.name === el ))
};

function getGaugePlotly(fields, divs) {
  const dataArr = getDataArr(fields, 'gaugeDataArr')

  dataArr.forEach((data, idx) => {
    const trace = [
      {
        type: "indicator",
        mode: "gauge+number",
        title: { text: data.text },
        gauge: {
          axis: { range: data.range },
          bar: { color: data.color},
          steps: data.steps,
          threshold: {
            line: { color: "red", width: 4 },
            thickness: 0.75,
            value: data.value,
          },
        },
      },
    ];
    Plotly.newPlot(divs[idx], trace, layout, config);
  })
};

function getHystoryPlotly(fields, divs) {
  const dataArr = getDataArr(fields, 'historyDataArr')

  dataArr.forEach((data, idx) => {
    const trace = {
      x: [],
      y: [],
      name: data.name,
      mode: "lines+markers",
      type: "line",
    };
    const historyLayout = {
      height: 300,
      title: {
        text: data.text,
      },
      font: {
        size: 14,
        color: "#808080",
      },
      colorway: [data.colorway],
    };
    Plotly.newPlot(divs[idx], [trace], historyLayout, config);
  })
};

function getDataForLineChart(dataArr, field) {
  return dataArr.map(item => item[field]);
};

function getDivs(selector) {
  const divs = [];
  const nodeEls = document.querySelectorAll(selector);
  nodeEls.forEach((el) => divs.push(el));
  return divs;
};

export { getFields, getDivs, getGaugePlotly, getHystoryPlotly, getDataForLineChart }