// Header Slider
var swiper = new Swiper(".header-slider", {
  speed: 500,
  spaceBetween: 30,
  centeredSlides: true,
  autoplay: {
    delay: 2500,
    disableOnInteraction: false,
  },
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
    renderBullet: (index, className) => `<span class="${className} custom-bullet"></span>`
  },
  navigation: {
    nextEl: ".button-next",
    prevEl: ".button-prev",
  },
  effect: "fade",
});



// Latest Products 
var swiper = new Swiper(".LatestProducts", {
  slidesPerView: 1,
  spaceBetween: 30,
  breakpoints: {
    350: {
      slidesPerView: 2,
      spaceBetween: 10,
    },
    640: {
      slidesPerView: 3,
      spaceBetween: 20,
    },
    768: {
      slidesPerView: 3,
      spaceBetween: 40,
    },
    1024: {
      slidesPerView: 4,
      spaceBetween: 20,
    },
    1200: {
      slidesPerView: 4,
      spaceBetween: 10
    },
    1260: {
      slidesPerView: 5,
      spaceBetween : 20
    }
  },
  loop: true,
  autoplay: {
    delay: 2000,
    disableOnInteraction: false,
  },
  speed: 1000,
  navigation: {
    nextEl: ".next-slide",
    prevEl: ".prev-slide",
  },
});

// Best-selling SLIDER
var swiper = new Swiper(".BestSelling", {
  slidesPerView: 1,
  spaceBetween: 30,
  breakpoints: {
    350: {
      slidesPerView: 2,
      spaceBetween: 10,
    },
    640: {
      slidesPerView: 3,
      spaceBetween: 20,
    },
    768: {
      slidesPerView: 3,
      spaceBetween: 40,
    },
    1024: {
      slidesPerView: 4,
      spaceBetween: 20,
    },
    1200: {
      slidesPerView: 4,
      spaceBetween: 10
    },
    1260: {
      slidesPerView: 5,
      spaceBetween : 20
    }
  },
  loop: true,
  autoplay: {
    delay: 1500,
    disableOnInteraction: false,
  },
  speed: 1000,
  navigation: {
    nextEl: ".next-slide-best",
    prevEl: ".prev-slide-best",
  },
});


// Offer
var swiper = new Swiper(".offerSlider", {
  slidesPerView: 1,
  spaceBetween: 30,
  loop : true ,
  breakpoints: {
    340: {
      slidesPerView: 1,
      spaceBetween: 30,
    },
    640: {
      slidesPerView: 2,
      spaceBetween: 20,
    },
    768: {
      slidesPerView: 3,
      spaceBetween: 40,
    },
    1024: {
      slidesPerView: 3,
      spaceBetween: 15,
    },
    1200: {
      slidesPerView: 4,
      spaceBetween: 20
    },
  },
  autoplay: {
    delay: 1500,
    disableOnInteraction: false,
  },
  speed: 1000,
});



var swiper = new Swiper(".porduct-details-slider", {
  spaceBetween: 20,
  pagination: {
    el: ".swiper-pagination",
  },
});