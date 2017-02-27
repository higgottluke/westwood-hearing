$('#enable-edit').click(function() {
  if ($("form input:first").is(':disabled')) {
    $('.form-control').prop('disabled', false);
  }
  else $('.form-control').prop('disabled', true);

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
