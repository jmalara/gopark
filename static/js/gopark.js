function sendPoint(type) {
  $("#worktoday").html("Selection Complete")
$.ajax({
  url: 'apipoints',
  type: 'POST',
  data: 'type=' + type,
  success: function(data) {
  //called when successful
  $("#leaderdiv").html(data);

},
  error: function(e) {
  //called when there is an error
  //console.log(e.message);
  }
});
}
