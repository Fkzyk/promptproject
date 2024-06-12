(function ($) {
    "use strict";

    // Spinner
    var spinner = function () {
        setTimeout(function () {
            if ($('#spinner').length > 0) {
                $('#spinner').removeClass('show');
            }
        }, 1);
    };
    spinner();

    // Initiate the wowjs
    new WOW().init();

    // Sticky Navbar
    var handleStickyNavbar = function () {
        if ($(window).scrollTop() > 45) {
            $('.navbar').addClass('sticky-top shadow-sm bg-white navbar-light').removeClass('bg-primary navbar-dark');
        } else {
            $('.navbar').removeClass('sticky-top shadow-sm bg-white navbar-light').addClass('bg-primary navbar-dark');
        }
    };

    // Initial check
    handleStickyNavbar();

    // Check on scroll
    $(window).scroll(handleStickyNavbar);

    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 100) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });

    // Testimonials carousel
    $(".testimonial-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1000,
        center: true,
        dots: false,
        loop: true,
        nav : true,
        navText : [
            '<i class="bi bi-chevron-left"></i>',
            '<i class="bi bi-chevron-right"></i>'
        ],
        responsive: {
            0:{
                items:1
            },
            576:{
                items:1
            },
            768:{
                items:2
            },
            992:{
                items:3
            }
        }
    });

    // Client carousel
    $(".client-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1000,
        margin: 90,
        dots: false,
        loop: true,
        nav : false,
        responsive: {
            0:{
                items:2
            },
            576:{
                items:3
            },
            768:{
                items:4
            },
            992:{
                items:5
            },
            1200:{
                items:6
            }
        }
    });

    // MDB Initialization
    if (typeof mdb !== 'undefined') {
        mdb.Ripple.init();
    }

    // Adjust container margin-top if the navbar is sticky
    $(document).ready(function() {
        if ($('.navbar').hasClass('sticky-top')) {
            $('body').css('padding-top', $('.navbar').outerHeight() + 'px'); // Adjust the padding-top of the body
        }
    });

})(jQuery);