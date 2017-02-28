var formEnabled = false;
$('#enable-edit').click(function() {
  if (formEnabled == false) {
    $('.form-control').prop('disabled', false);
    formEnabled = true;
  }
  else {
    $('.form-control').prop('disabled', true);
    formEnabled = false;
  }

});

$(document).ready(function() {
	// get current URL path and assign 'active' class
	var pathname = window.location.pathname;
	$('.nav > li > a[href="'+pathname+'"]').parent().addClass('active');
})

$(document).ready( function () {
    $('#datatables').DataTable();
    $('#fullCalendar').fullCalendar({
    // put your options and callbacks here
    })
    $('.datepicker').datepicker();
} );
