google.charts.load('current', {
  'packages': ['geochart'],
  'mapsApiKey': 'AIzaSyD-9tSrke72PouQMnMX-a7eZSW0jkFMBWY'
});

$.ajax({
  url: "static/resources/Happiness_2019.csv",
  async: true,
  success: function (csvData) {
    indicator = $.csv.toArrays(csvData, { onParseValue: $.csv.hooks.castToScalar });
  },
  dataType: "text",
  complete: function () {
    
    google.charts.setOnLoadCallback(drawRegionsMap);
    
    function drawRegionsMap() {
      var data = google.visualization.arrayToDataTable(indicator);
    
      var options = {
        colorAxis: {colors: ['white', 'gold']},
      };
    
      var chart = new google.visualization.GeoChart(document.getElementById('map_div'));
    
      chart.draw(data, options);
    }

  }
});
