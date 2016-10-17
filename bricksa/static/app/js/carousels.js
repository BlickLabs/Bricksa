(function () {
  'use strict';
  $('#banners-carousel').slick({
    prevArrow: '', 
    nextArrow: '<a href="#" class="arrow-next"></a>'
  });
  $('#project-carousel').slick({
    prevArrow: '', 
    nextArrow: '<a href="#" class="arrow-next"></a>',
    slidesToShow: 2,
    responsive: [
      {
        breakpoint: 720,
        settings: {
          slidesToShow: 1
        }
      }
    ]
  });
})();