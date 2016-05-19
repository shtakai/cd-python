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
  index();
  getNew();

  $(document).on('submit', 'form', function (e) {
    e.preventDefault();
    $.ajax({
      url: $(this).attr('action'),
      method: $(this).attr('method'),
      data: $(this).serialize(),
      success: function (data) {
        $('#notes').html(data);
        $('#title').val('');
        $('#description').val('');
      }
    })
    return false;
  });
});

