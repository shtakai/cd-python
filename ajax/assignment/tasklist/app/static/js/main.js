function index() {
  $.ajax({
    url: '/tasks',
    method: 'GET',
    success: function (data) {
      $('#tasks').html(data);
    }
  });
}

function getNew() {
  $.ajax({
    url: '/tasks/new',
    method: 'GET',
    success: function (data) {
      $('#new').html(data);
    }
  });
}

function setFinishedColor() {
  $('div#tasks').each(function (data) {
    console.log($(this));
  })


}



$(document).ready(function () {
  console.log('emit');
  index();
  getNew();
  //setFinishedColor();
  $(document).on('click', 'input[type=checkbox]', function (e) {
    //console.log($(this).prop('checked'));
    //console.log($(this).prop('id'));
    if($(this).prop('checked')==true){
    $(this).parent().css('color', 'gray');
    }else{
    $(this).parent().css('color', 'black');
    }
  });
  $(document).on('submit', 'form', function (e) {
    e.preventDefault();
    $.ajax({
      url: $(this).attr('action'),
      method: $(this).attr('method'),
      data: $(this).serialize(),
      success: function (data) {
        $('#tasks').html(data);
        $('#name').val('');
      }
    })
    return false;
  });
});

