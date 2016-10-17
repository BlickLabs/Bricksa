(function () {
  var mobile = window.matchMedia('(max-width: 768px)');

  function detectTouch(e) {
    if (!$(e.target).is('#navbar .menu-trigger') && !$(e.target).is('#navbar .menu-container') && !$(e.target).closest('#navbar .menu-container').length && $('#navbar .menu-container').hasClass('active')) {
      $('#navbar .menu-container').removeClass('active');
      $('body').removeClass('noscroll');
    }
  }

  function detectClick() {
    if ($('#navbar .menu-container').hasClass('active')) {
      $('#navbar .menu-container').removeClass('active');
      $('body').removeClass('noscroll');
    } else {
      $('#navbar .menu-container').addClass('active');
      $('body').addClass('noscroll');
    }
  }

  if (mobile.matches) {
    $('body')[0].addEventListener('touchstart', detectTouch, false);
    $('#navbar .menu-trigger').click(detectClick);
  } else {
    $('body')[0].removeEventListener('touchstart', detectTouch, false);
    $('#navbar .menu-trigger').unbind('click');
    $('body').removeClass('noscroll');
  }

  $(window).resize(function () {
    $('body')[0].removeEventListener('touchmove', detectTouch, false);
    $('#navbar .menu-trigger').unbind('click');
    $('body').removeClass('noscroll');
    $('#navbar .menu-container').removeClass('active');

    if (mobile.matches) {
      $('body')[0].addEventListener('touchmove', detectTouch, false);
      $('#navbar .menu-trigger').click(detectClick);
    }
  });
})();
