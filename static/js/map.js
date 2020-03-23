var url = `../resources/Happiness_2019.csv`;

google.charts.load('current', {
  'packages': ['geochart'],
  'mapsApiKey': 'AIzaSyD-9tSrke72PouQMnMX-a7eZSW0jkFMBWY',
  callback: function () {
    $.get(url, function (csvString) {

      var arrayData = $.csv.toArrays(csvString, { onParseValue: $.csv.hooks.castToScalar });
      var data = new google.visualization.arrayToDataTable(arrayData);
      
      var options = {}
      
      var chart = new google.visualization.GeoChart(document.getElementById('map_div'));

      chart.draw(data, options);
    })
  }
})
}