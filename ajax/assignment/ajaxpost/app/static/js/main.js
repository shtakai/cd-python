$(document).ready(function () {

  $('#textarea1').trigger('autoresize');

  $('form#noteform').click(function (e) {
    console.log('clicked');
    $.post('/notes/create', $(this).serialize(), function(res) {
      console.log($('form#noteform'));
      console.log(res);
      $('#posts').html(res);
      $('#description').val("");

    });
    return false;
  });


});

