
$(document).ready(function(){
  var img_html = "";
  img_html += '<ul class="list-inline list-unstyled">';
  for(var i = 1; i <= 151; i++){
    img_html += '<li class="col-sm-2"><img class="pokeimg" id="' + i + '" src="http://pokeapi.co/media/img/' + i + '.png"></li>';
    //img_html += 'i' + i;
  }
  img_html += "</ul>";
  //console.log(img_html);
  $('#pokemon').html(img_html);

  $('.pokeimg').click(function (e) {
    console.log(this.id);
    var id = this.id
    $.get("http://pokeapi.co/api/v1/pokemon/" + this.id +"/", function(res) {
      console.log(res);
      var html_str = "";
      html_str += "<h3>" + res.name + "</h3>";
      html_str += '<img src="http://pokeapi.co/media/img/' + id + '.png">';
      html_str += "<h4>Types</h4>";
      html_str += "<ul>";
      for(var i = 0; i < res.types.length; i++) {
        html_str += "<li>" + res.types[i].name + "</li>";
      }
      html_str += "</ul>";
      html_str += "<h4>Height</h4>" + res.height;
      html_str += "<h4>Weight</h4>" + res.weight;

      console.log(html_str);
      $("#info").html(html_str);
    }, "json");
  });

});
