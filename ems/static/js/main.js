let  leave = document.getElementById('leave').value
let Workdays =  365 - leave; 
var xValues = ["Leaves", "Workdays"];
var yValues = [leave, Workdays];
var barColors = [
  "#e62291",
  "#33edc1",
];

new Chart("myChart", {
  type: "pie",
  data: {
    labels: xValues,
    datasets: [{
      backgroundColor: barColors,
      data: yValues
    }]
  },
  options: {
    title: {
      display: true,
      text: "Annual Work Report"
    }
  }
});

