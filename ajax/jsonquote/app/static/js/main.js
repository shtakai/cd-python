// once the document is loaded
$(document).ready(function(){
  // we'll add a click handler to the button
  $('#get_all_button').click(function(){
    // this is the jQuery get function, which we'll use to send Ajax requests
    // to this function we are passing 3 arguments
    // a url, function, and the dataType parameter
    $.get('/quotes/index_json', function(res) {
      // the function will send a request to the above url and get a response
      // which we will store in the variable 'res'
      var htmlStr = ""; // we create an empty string
      // then loop through our res and create a string of html tags below
      for(var i = 0; i < res['quotes'].length; i++) {
        htmlStr += "<div class='quote'>";
        htmlStr += "<h2>" + res.quotes[i].author + "</h2>";
        htmlStr += "<p>" + res.quotes[i].quote + "</p>";
        htmlStr += "</div>";
      }
      // uncomment the line below to see what our string looks like
      // console.log(htmlStr);
      // insert our string into our document using jQuery
      $('#quotes').html(htmlStr);
    }, 'json');
  });
});
