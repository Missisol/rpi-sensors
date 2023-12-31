import { config, lineChartDataArr, getFields, getFilteredDataArr} from './commonData.js';

function getProcessedFields(str) {
  let obj = {};
  const arr = getFields(str);
  arr.forEach((field) => {
    obj[field] = [`min_${field}`, `max_${field}`];
  })

  return obj;
};

function getDeltaPlotly(fields, divs) {
  const dataArr = getFilteredDataArr(fields, lineChartDataArr)
  dataArr.forEach((data, idx) => {
    const trace1 = {
      x: [],
      y: [],
      name: `min ${data.legend}`,
      mode: "lines+markers",
      line: {
        dash: 'dot',
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
      },
      colorway: [data.color],
    };
  
    Plotly.newPlot(divs[idx], traces, layout, config);
  });
};

export { getProcessedFields, getDeltaPlotly }