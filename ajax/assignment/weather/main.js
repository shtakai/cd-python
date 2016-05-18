$(document).ready(function(){
  $('#search').click(function (e) {
    var area = $('#area').val();
    console.log(area);
    $.ajax({
      url: 'http://api.openweathermap.org/data/2.5/forecast?q=' + area + '&units=imperial&mode=json&appid=' + apikey,
      method: 'GET',
      success: function (res) {
        htmlStr = "";
        htmlStr += '<h2>' + res.city.name + '</h2>';
        htmlStr += '<h3>Temperature:' + res.list[0].main.temp + ' F</h3>'
        $('#weather').html(htmlStr);
        return false;
      }
    }, 'json');
  })
});
