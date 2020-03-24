// require('dotenv').config();

var url = "static/resources/Happiness_2019.csv";

google.charts.load('current', {
  'packages': ['geochart'],
  'mapsApiKey': 'AIzaSyD-9tSrke72PouQMnMX-a7eZSW0jkFMBWY',
  // 'mapsApiKey': process.env.MAPS_API_KEY,

  callback: function () {
    $.get(url, function (csvData) {

      var arrayData = $.csv.toArrays(csvData, { onParseValue: $.csv.hooks.castToScalar });
      var data = google.visualization.arrayToDataTable(arrayData);
    
      var options = {
        colorAxis: {colors: ['white', 'gold']},
      };
    
      var chart = new google.visualization.GeoChart(document.getElementById('map_div'));
    
      chart.draw(data, options);

    })
  }

});
