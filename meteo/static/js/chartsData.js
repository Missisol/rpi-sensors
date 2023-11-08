export const gaugeDataArr = [
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

export const layout = { 
  width: 300,
  height: 250, 
  margin: { t: 30, b: 30, l: 30, r: 30 },
};

export const config = {
  responsive: true,
  displayModeBar: false,
};

export const historyDataArr = [
  { name: 'temperature', text: 'Температура', colorway: '3ba639' },
  { name: 'humidity', text: 'Влажность', colorway: '047df3' },
  { name: 'pressure', text: 'Давление', colorway: '808080'},
];