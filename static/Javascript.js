$(document).ready(function () {
  $('#myForm input').keydown(function (e) {
    if (e.keyCode == 13) {

      if ($(':input:eq(' + ($(':input').index(this) + 1) + ')').attr('type') == 'submit') {// check for submit button and submit form on enter press
        return true;
      }

      $(':input:eq(' + ($(':input').index(this) + 1) + ')').focus();

      return false;
    }

  });
});