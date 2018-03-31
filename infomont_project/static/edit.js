$('body').on('dblclick', '[data-editable]', function(){
var $el = $(this);

  var $input = $('<input class="form-control" />').val( $el.text());
  $el.replaceWith( $input );

  var save = function(){
    var $p =  $('<div data-editable/>').text($input.val());
    $input.replaceWith( $p );
  };

  /**
    We're defining the callback with `one`, because we know that
    the element will be gone just after that, and we don't want
    any callbacks leftovers take memory.
    Next time `p` turns into `input` this single callback
    will be applied again.
  */
  $input.one('blur', save).focus();
});