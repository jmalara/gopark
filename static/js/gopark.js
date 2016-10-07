function sendPoint(type) {
  $("#buttons").hide()
  $("#complete").css("display", "block");
  $("#completext").html("Thank you for choosing " + type + " today. Don't forget to check in tomorrow!")
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
function refreshPoint() {
$.ajax({
  url: 'apipoints',
  type: 'POST',
  data: 'type=0',
  success: function(data) {
$("#leaderdiv").html(data);

},
  error: function(e) {
  }
});
}

$(document).ready(function(){
setInterval(refreshPoint,5000);
});
