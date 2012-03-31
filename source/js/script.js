/* Author:

*/
$(document).ready(function() {

  var first = $('.trivia:first')

  $('#me').on('animationend.test', '.trivia', function(e) {

    $(this).removeClass('test');

    var next = $(this).next();
    if (next.length === 0) {
      first.addClass('test');
    } else {
      next.addClass('test');
    }

    e.stopPropagation();
  });
});
