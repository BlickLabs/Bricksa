(function () {
  'use strict';
  $('#banners-carousel').slick({
    prevArrow: '', 
    nextArrow: '<a href="#" class="arrow-next"></a>',
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 6000
  });
  $('#project-carousel').slick({
    prevArrow: '', 
    nextArrow: '<a href="#" class="arrow-next"></a>',
    slidesToShow: 2,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 6000,
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