function sendPoint(type) {
  user = readCookie()
  $("#worktoday").html("Selection Complete")
$.ajax({
  url: 'apipoints',
  type: 'POST',
  data: 'user=' + user + '&type=' + type,
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

function readCookie(name) {
  return 'jeremy@malara.net'
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for(var i=0;i < ca.length;i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1,c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
    }
    return null;
}