
let  active = document.getElementById('active').value
let notactive = document.getElementById('notactive').value
var xValues = ["Active", "Not Active"];
var yValues = [active, notactive];
var barColors = [
    "#80ED99",
    "#ff0a54",
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
      text: "Employee Status"
    }
  }
});