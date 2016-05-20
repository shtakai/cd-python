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

}


$(document).ready(function () {
  console.log('emit');
  //index();
  //getNew();
  setFinishedColor();
  //$(document).on('submit', 'form', function (e) {
    //e.preventDefault();
    //$.ajax({
      //url: $(this).attr('action'),
      //method: $(this).attr('method'),
      //data: $(this).serialize(),
      //success: function (data) {
        //$('#tasks').html(data);
        //$('#title').val('');
        //$('#description').val('');
      //}
    //})
    //return false;
  //});
});

