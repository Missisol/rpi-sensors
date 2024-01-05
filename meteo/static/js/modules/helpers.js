const minDate = '2023-11-08'

const getDate = () => {
  const currentDate = new Date();
  const year = currentDate.getFullYear();
  const day = currentDate.getDay() < 10 ? `0${currentDate.getDay()}` : currentDate.getDay();
  const month = currentDate.getMonth() < 9 ? `0${currentDate.getMonth() + 1}` : currentDate.getMonth() + 1;
  return { year, month, day };
}

const getFormettedDate = () => {
  const { year, month, day } = getDate();
  return `${year}-${month}-${day}`;
}

export {
  minDate,
  getFormettedDate,
}