(function($) {
    "use strict";

    $(document).ready(function() {

        /*
        ========================================
            input search open item
        ========================================
        */
        $(document).on('keyup change', '#search_form_input', function(event) {

            let input_values = $(this).val();

            if (input_values.length > 0) {
                $('#search_suggestions_wrap, .search-suggestion-overlay').addClass("show");
            } else {
                $('#search_suggestions_wrap, .search-suggestion-overlay').removeClass("show");
            }
        });
        $(document).on('click', '.search-suggestion-overlay, .search-click-icon', function() {
            $('#search_suggestions_wrap, .search-suggestion-overlay').removeClass('show')
        })
        $(document).on('click', '.search-click-icon', function() {
            $('.search-show').toggleClass('open')
        })
        $(document).on('click', '.suggestions-icon-close, .search-suggestion-overlay', function() {
            $('.search-show').removeClass('open')
            $('#search_suggestions_wrap, .search-suggestion-overlay').removeClass('show')
        })


        /* 
        ========================================
            Navbar Toggler
        ========================================
        */
        $(document).on('click', '.navbar-toggler', function() {
            $(".navbar-toggler").toggleClass("active");
        });

        $(document).on('click', '.click-nav-right-icon', function() {
            $(".show-nav-content").toggleClass("show");
        });

        /* 
        ========================================
            Show nav right content
        ========================================
        */
        $(document).on('click', '.click-content-show', function() {
            $(".right-contents-show").toggleClass("show");
        });

        /* 
        ========================================
            Shop Responsive Sidebar
        ========================================
        */
        $(document).on('click', '.shop-close-content-icon, .responsive-overlay', function() {
            $('.shop-close-content, .responsive-overlay').removeClass('active');
        });
        $(document).on('click', '.shop-icon-sidebar', function() {
            $('.shop-close-content, .responsive-overlay').addClass('active');
        });

        /*
        ========================================
            Magnific Popup Js
        ========================================
        */
        $('.gallery-popup, .gallery-popup-two').magnificPopup({
            type: 'image',
            gallery: {
                enabled: true,
            }
        });

        /*
        ========================================
            Masonry js
        ========================================
        */
        $('.imgLoaded').imagesLoaded(function() {
            $('.masonry-grid').isotope({
                itemSelector: '.grid-item',
                percentPosition: true,
                masonry: {
                    // use outer width of grid-sizer for columnWidth
                    columnWidth: '.grid-item'
                }
            })
        });

        /* 
        ========================================
            Tab
        ========================================
        */
        $(document).on('click', 'ul.tabs li', function() {
            var tab_id = $(this).attr('data-tab');

            $('ul.tabs li').removeClass('active');
            $('.tab-content-item').removeClass('active');

            $(this).addClass('active');
            $("#" + tab_id).addClass('active');
        });

        /* 
        ========================================
            Pagination On Click Js
        ========================================
        */
        $(document).on('click', '.pagination-list-item', function() {
            $(this).siblings().removeClass('active');
            $(this).addClass('active');
        });
        /* Next Previous btn Click */
        $(document).on('click', '.pagination-list-item-next', function() {
            $(this).parent().find('.pagination-list-item.active').next('.pagination-list-item').addClass('active');
            $(this).parent().find('.pagination-list-item.active').prev('.pagination-list-item').removeClass('active');
        });
        $(document).on('click', '.pagination-list-item-prev', function() {
            $(this).parent().find('.pagination-list-item.active').prev('.pagination-list-item').addClass('active');
            $(this).parent().find('.pagination-list-item.active').next('.pagination-list-item').removeClass('active');
        });

        /* 
        ========================================
            Hover Slide Js
        ========================================
        */
        $(document).on('mouseenter', '.custom-tab ul.tab-menu li', function(r) {
            var tab = $(this).closest('.custom-tab'),
                index = $(this).closest('li').index();
            tab.find('li').siblings('li').removeClass('active');
            $(this).closest('li').addClass('active');
            tab.find('.tab-area').find('div.tab-item').not('div.tab-item:eq(' + index + ')').hide().siblings().removeClass('active');
            tab.find('.tab-area').find('div.tab-item:eq(' + index + ')').show().addClass('active');
            r.preventDefault();
        });

        /* 
        ========================================
            Product Quantity js
        ========================================
        */
        $(function() {

            $(document).on('click', '.plus', function() {
                var selectedInput = $(this).prev('.quantity-input');
                // if (selectedInput.val() < 50) {
                selectedInput[0].stepUp(1);
                // }
            });
            $(document).on('click', '.minus', function() {
                var selectedInput = $(this).next('.quantity-input');
                if (selectedInput.val() > 1) {
                    selectedInput[0].stepDown(1);
                }
            });

        });

        /* 
        ========================================
            Click Active Class
        ========================================
        */
        $(document).on('click', '.active-list .item', function() {
            $(this).siblings().removeClass('active');
            $(this).toggleClass('active');
        });

        /*-------------------------------
            Click Slide Open Close
        ------------------------------*/
        $(document).on('click', '.single-shop-left-title .title', function(e) {
            var shopTitle = $(this).parent('.single-shop-left-title');
            if (shopTitle.hasClass('open')) {
                shopTitle.removeClass('open');
                shopTitle.find('.single-shop-left-inner').removeClass('open');
                shopTitle.find('.single-shop-left-inner').slideUp(300, "swing");
            } else {
                shopTitle.addClass('open');
                shopTitle.children('.single-shop-left-inner').slideDown(300, "swing");
                shopTitle.siblings('.single-shop-left-title').children('.single-shop-left-inner').slideUp(300, "swing");
                shopTitle.siblings('.single-shop-left-title').removeClass('open');
            }
        });

        /*-------------------------------
            Dashboard ReservationIcon
        ------------------------------*/
        $(document).on('click', '.single-reservation-expandIcon', function(e) {
            var shopTitle = $(this).parent('.single-reservation');
            if (shopTitle.hasClass('open')) {
                shopTitle.removeClass('open');
                shopTitle.find('.single-reservation-inner').removeClass('open');
                shopTitle.find('.single-reservation-inner').slideUp(600);
            } else {
                shopTitle.addClass('open');
                shopTitle.children('.single-reservation-inner').slideDown(600);
                shopTitle.siblings('.single-reservation').find('.single-reservation-inner').slideUp(600);
                shopTitle.siblings('.single-reservation').removeClass('open');
            }
        });

        /* 
        ========================================
            Nice Select
        ========================================
        */
        $('.js-select').niceSelect();

        /* 
        ========================================
            Click Active Class
        ========================================
        */
        $(document).on('click', '.popup-overlay, .popup-close', function() {
            $('.popup-fixed, .popup-overlay').removeClass('popup-active');
        });
        $(document).on('click', '.popup-click', function() {
            $('.popup-fixed, .popup-overlay').toggleClass('popup-active');
        });

        /*
        ========================================
           Faq accordion
        ========================================
        */
        $('.faq-contents .faq-title').on('click', function(e) {
            var element = $(this).parent('.faq-item');
            if (element.hasClass('open')) {
                element.removeClass('open');
                element.find('.faq-panel').removeClass('open');
                element.find('.faq-panel').slideUp(300, "swing");
            } else {
                element.addClass('open');
                element.children('.faq-panel').slideDown(300, "swing");
                element.siblings('.faq-item').children('.faq-panel').slideUp(300, "swing");
                element.siblings('.faq-item').removeClass('open');
                element.siblings('.faq-item').find('.faq-title').removeClass('open');
                element.siblings('.faq-item').find('.faq-panel').slideUp(300, "swing");
            }
        });

        /* 
        ========================================
            Dropdown Submenu
        ========================================
        */

        $(document).on('click', '.dashboard-list .has-children a', function(e) {
            var sh = $(this).parent('.has-children');
            if (sh.hasClass('open')) {
                sh.removeClass('open');
                sh.find('.submenu').children('.has-children').removeClass("open"); //2nd children remove 
                sh.find('.submenu').removeClass('open');
                sh.find('.submenu').slideUp(300, "swing");
            } else {
                sh.addClass('open');
                sh.children('.submenu').slideDown(300, "swing");
                sh.siblings('.has-children').children('.submenu').slideUp(300, "swing");
                sh.siblings('.has-children').removeClass('open');
                sh.siblings().find('.submenu').children('.has-children').removeClass('open'); //2nd Submenu children remove 
                sh.siblings().find('.submenu').slideUp(300, "swing"); //2nd Submenu children Slide Up Down 
            }
        });

        /* 
        ========================================
            Dashboard Responsive Sidebar
        ========================================
        */
        $(document).on('click', '.close-bars, .body-overlay', function() {
            $('.dashboard-close, .dashboard-left-content, .body-overlay').removeClass('active');
        });
        $(document).on('click', '.sidebar-icon', function() {
            $('.dashboard-close, .dashboard-left-content, .body-overlay').toggleClass('active');
        });



        /*
        ========================================
            Blog Details Title open Close
        ========================================
        */

        $(document).on('click', '.blog-details-side-title .title', function(e) {
            var element = $(this).parent('.blog-details-side-title');
            if (element.hasClass('open')) {
                element.removeClass('open');
                element.find('.blog-details-side-inner').slideUp(300, "swing");
            } else {
                element.addClass('open');
                element.children('.blog-details-side-inner').slideDown(300, "swing");
                element.siblings('.blog-details-side-title').children('.blog-details-side-inner').slideUp(300, "swing");
                element.siblings('.blog-details-side-title').removeClass('open');
            }
        });

        /* 
        ========================================
            Bootstrap Tooltip
        ========================================
        */
        var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
        var tooltipList = tooltipTriggerList.map(function(tooltipTriggerEl) {
            return new bootstrap.Tooltip(tooltipTriggerEl)
        });

        /* 
        ========================================
            Range Slider
        ========================================
        */
        var i = document.querySelector(".ui-range-slider");
        if (void 0 !== i && null !== i) {
            var j = parseInt(i.parentNode.getAttribute("data-start-min"), 10),
                k = parseInt(i.parentNode.getAttribute("data-start-max"), 10),
                l = parseInt(i.parentNode.getAttribute("data-min"), 10),
                m = parseInt(i.parentNode.getAttribute("data-max"), 10),
                n = parseInt(i.parentNode.getAttribute("data-step"), 10),
                o = document.querySelector(".ui-range-value-min span"),
                p = document.querySelector(".ui-range-value-max span"),
                q = document.querySelector(".ui-range-value-min input"),
                r = document.querySelector(".ui-range-value-max input");
            noUiSlider.create(i, {
                start: [j, k],
                connect: !0,
                step: n,
                range: {
                    min: l,
                    max: m
                }
            }), i.noUiSlider.on("update", function(a, b) {
                var c = a[b];
                b ? (p.innerHTML = Math.round(c), r.value = Math.round(c)) : (o.innerHTML = Math.round(c), q.value = Math.round(c))
            })
        }


        /*
        ========================================
            wow js init
        ========================================
        */
        new WOW().init();

        /* 
        ========================================
            Password Show Hide On Click
        ========================================
        */

        $(document).on("click", ".toggle-password", function(e) {
            e.preventDefault();
            let inputPass = $(this).parent().find("input");
            $(this).toggleClass("show-pass");
            if (inputPass.attr("type") == "password") {
                inputPass.attr("type", "text");
            } else {
                inputPass.attr("type", "password");
            }
        });

        /* 
        ========================================
            Select Country Code Js
        ========================================
        */
        // Vanilla Javascript
        if (document.querySelector('#phone') != null) {
            let TellInput = document.querySelector("#phone");
            window.intlTelInput(TellInput, {
                allowDropdown: true,
                excludeCountries: ["bn"],
            });
        }

        /* 
        ========================================
            Radio box active Class Js
        ========================================
        */
        $(document).on('click', '.custom-radio-single', function(e) {
            $(this).siblings().removeClass('active');
            $(this).addClass('active');
        });

        /*      
        ========================================
            Flat Picker js
        ========================================
        */
        $(".date-picker").flatpickr({
            mode: "single",
            enableTime: true,
            dateFormat: "d-m-Y H:i",
            altInput: true,
            altFormat: "F j, Y",
            time_12hr: true,
        });

        /*
        ========================================
            container
        ========================================
        */
        $(".newsletter-area .container").length && $(window).on("scroll", function() {
            ! function(t, a = 0) {
                var i = $(window).scrollTop(),
                    o = i + $(window).height(),
                    s = $(t).offset().top;
                return s + $(t).height() - parseInt(a) <= o && s >= i
            }(".newsletter-area .container", 200) ? $(".newsletter-area .container").removeClass("container-fluid"): $(".newsletter-area .container").addClass("container-fluid")
        })

        /*
        ========================================
            Global Slider Init
        ========================================
        */
        var globalSlickInit = $('.global-slick-init');
        if (globalSlickInit.length > 0) {
            //todo have to check slider item 
            $.each(globalSlickInit, function(index, value) {
                if ($(this).children('div').length > 1) {
                    //todo configure slider settings object
                    var sliderSettings = {};
                    var allData = $(this).data();
                    var infinite = typeof allData.infinite == 'undefined' ? false : allData.infinite;
                    var arrows = typeof allData.arrows == 'undefined' ? false : allData.arrows;
                    var autoplay = typeof allData.autoplay == 'undefined' ? false : allData.autoplay;
                    var focusOnSelect = typeof allData.focusonselect == 'undefined' ? false : allData.focusonselect;
                    var swipeToSlide = typeof allData.swipetoslide == 'undefined' ? false : allData.swipetoslide;
                    var slidesToShow = typeof allData.slidestoshow == 'undefined' ? 1 : allData.slidestoshow;
                    var slidesToScroll = typeof allData.slidestoscroll == 'undefined' ? 1 : allData.slidestoscroll;
                    var speed = typeof allData.speed == 'undefined' ? '500' : allData.speed;
                    var dots = typeof allData.dots == 'undefined' ? false : allData.dots;
                    var cssEase = typeof allData.cssease == 'undefined' ? 'linear' : allData.cssease;
                    var prevArrow = typeof allData.prevarrow == 'undefined' ? '' : allData.prevarrow;
                    var nextArrow = typeof allData.nextarrow == 'undefined' ? '' : allData.nextarrow;
                    var centerMode = typeof allData.centermode == 'undefined' ? false : allData.centermode;
                    var centerPadding = typeof allData.centerpadding == 'undefined' ? false : allData.centerpadding;
                    var rows = typeof allData.rows == 'undefined' ? 1 : parseInt(allData.rows);
                    var autoplay = typeof allData.autoplay == 'undefined' ? false : allData.autoplay;
                    var autoplaySpeed = typeof allData.autoplayspeed == 'undefined' ? 2000 : parseInt(allData.autoplayspeed);
                    var lazyLoad = typeof allData.lazyload == 'undefined' ? false : allData.lazyload; // have to remove it from settings object if it undefined
                    var appendDots = typeof allData.appenddots == 'undefined' ? false : allData.appenddots;
                    var appendArrows = typeof allData.appendarrows == 'undefined' ? false : allData.appendarrows;
                    var asNavFor = typeof allData.asnavfor == 'undefined' ? false : allData.asnavfor;
                    var verticalSwiping = typeof allData.verticalswiping == 'undefined' ? false : allData.verticalswiping;
                    var vertical = typeof allData.vertical == 'undefined' ? false : allData.vertical;
                    var fade = typeof allData.fade == 'undefined' ? false : allData.fade;
                    var rtl = typeof allData.rtl == 'undefined' ? false : allData.rtl;
                    var responsive = typeof $(this).data('responsive') == 'undefined' ? false : $(this).data('responsive');
                    //slider settings object setup
                    sliderSettings.infinite = infinite;
                    sliderSettings.arrows = arrows;
                    sliderSettings.autoplay = autoplay;
                    sliderSettings.focusOnSelect = focusOnSelect;
                    sliderSettings.swipeToSlide = swipeToSlide;
                    sliderSettings.slidesToShow = slidesToShow;
                    sliderSettings.slidesToScroll = slidesToScroll;
                    sliderSettings.speed = speed;
                    sliderSettings.dots = dots;
                    sliderSettings.cssEase = cssEase;
                    sliderSettings.prevArrow = prevArrow;
                    sliderSettings.nextArrow = nextArrow;
                    sliderSettings.rows = rows;
                    sliderSettings.autoplaySpeed = autoplaySpeed;
                    sliderSettings.autoplay = autoplay;
                    sliderSettings.verticalSwiping = verticalSwiping;
                    sliderSettings.vertical = vertical;
                    sliderSettings.rtl = rtl;
                    if (centerMode != false) {
                        sliderSettings.centerMode = centerMode;
                    }
                    if (centerPadding != false) {
                        sliderSettings.centerPadding = centerPadding;
                    }
                    if (lazyLoad != false) {
                        sliderSettings.lazyLoad = lazyLoad;
                    }
                    if (appendDots != false) {
                        sliderSettings.appendDots = appendDots;
                    }
                    if (appendArrows != false) {
                        sliderSettings.appendArrows = appendArrows;
                    }
                    if (asNavFor != false) {
                        sliderSettings.asNavFor = asNavFor;
                    }
                    if (fade != false) {
                        sliderSettings.fade = fade;
                    }
                    if (responsive != false) {
                        sliderSettings.responsive = responsive;
                    }
                    $(this).slick(sliderSettings);
                }
            });
        }

        /*
        ========================================
            Mouse Cursor Js
        ========================================
        */
        var myCursor = $('.mouse-move');
        if (myCursor.length) {
            if ($('body')) {
                const e = document.querySelector('.mouse-inner'),
                    t = document.querySelector('.mouse-outer');
                let n, i = 0,
                    o = !1;
                window.onmousemove = function(s) {
                    o || (t.style.transform = "translate(" + s.clientX + "px, " + s.clientY + "px)"), e.style.transform = "translate(" + s.clientX + "px, " + s.clientY + "px)", n = s.clientY, i = s.clientX
                }, $('body').on("mouseenter", "a, .cursor-pointer", function() {
                    e.classList.add('mouse-hover'), t.classList.add('mouse-hover')
                }), $('body').on("mouseleave", "a, .cursor-pointer", function() {
                    $(this).is("a") && $(this).closest(".cursor-pointer").length || (e.classList.remove('mouse-hover'), t.classList.remove('mouse-hover'))
                }), e.style.visibility = "visible", t.style.visibility = "visible"
            }
        }

        /* 
        ========================================
            back to top
        ========================================
        */
        $(document).on('click', '.back-to-top', function() {
            $("html,body").animate({
                scrollTop: 0
            }, 700);
        });

    });
    /* 
    ========================================
        back to top
    ========================================
    */
    $(window).on('scroll', function() {
        //back to top show/hide
        var ScrollTop = $('.back-to-top');
        if ($(window).scrollTop() > 200) {
            ScrollTop.fadeIn(10);
        } else {
            ScrollTop.fadeOut(10);
        }
    });


})(jQuery);