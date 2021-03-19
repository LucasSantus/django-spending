
//Floating Action Bottom
document.addEventListener('DOMContentLoaded', function() {
  var elems = document.querySelectorAll('.fixed-action-btn');
  var instances = M.FloatingActionButton.init(elems, options);
});

  // Or with jQuery

$(document).ready(function(){
  $('.fixed-action-btn').floatingActionButton();
});