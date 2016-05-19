function index() {
  $.ajax({
    url: '/notes',
    method: 'GET',
    success: function (data) {
      $('#notes').html(data);
    }
  });
}

function getNew() {
  $.ajax({
    url: '/notes/new',
    method: 'GET',
    success: function (data) {
      $('#new').html(data);
    }
  });
}




$(document).ready(function () {

  console.log('emit');

  index();
  getNew();


});

