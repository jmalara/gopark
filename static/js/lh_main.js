// NAV Menu 
$(document).ready(function () {
  thePage = document.location.href.match(/[^\/]+$/)[0]
  if(thePage == '') thePage = 'dashboard'
  $(".nav li").removeClass("active");
  $('#' + thePage).addClass('active');

  
});