$(document).ready(function () {

  $('#textarea1').trigger('autoresize');

  $('#postnote').click(function (e) {
    console.log('clicked');
    $.post('/notes/create', $('form#noteform').serialize(), function(res) {
      console.log($('form#noteform'));
      //console.log(res);
      $('#posts').html(res);
      $('#description').val("");

    });
    return false;
  });


});

