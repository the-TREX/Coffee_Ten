document.addEventListener('DOMContentLoaded', function () {
    // مدیریت حالت تم (تیره/روشن)
    function initTheme() {
        const theme = localStorage.getItem('theme');
        const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;

        if (theme === 'dark' || (!theme && prefersDark)) {
            document.documentElement.classList.add('dark');
        }
    }

    // تابع برای تغییر تم
    function toggleTheme() {
        document.documentElement.classList.toggle('dark');
        localStorage.setItem('theme', document.documentElement.classList.contains('dark') ? 'dark' : 'light');
    }

    // مدیریت منوی موبایل
    function setupMobileMenu() {
        const mobileMenu = document.querySelector('.mobile-menu');
        const openBtn = document.querySelector('.mobile-menu__open-icon');
        const closeBtn = document.querySelector('.mobile-menu__close-icon');
        const overlay = document.querySelector('.overlay');

        if (!mobileMenu || !openBtn || !closeBtn || !overlay) return;

        function openMenu() {
            overlay.classList.remove('hidden');
            overlay.classList.add('flex');
            mobileMenu.classList.remove('-right-64');
            mobileMenu.classList.add('right-0');
        }

        function closeMenu() {
            overlay.classList.add('hidden');
            overlay.classList.remove('flex');
            mobileMenu.classList.remove('right-0');
            mobileMenu.classList.add('-right-64');
        }

        openBtn.addEventListener('click', openMenu);
        closeBtn.addEventListener('click', closeMenu);
        overlay.addEventListener('click', closeMenu);
    }

    // مدیریت سبد خرید
    function setupShoppingCart() {
        const cart = document.querySelector('.shopping-cart');
        const openBtns = document.querySelectorAll('.open-shopping-cart__btn');
        const closeBtns = document.querySelectorAll('.close-shopping-cart__btn');
        const overlay = document.querySelector('.overlay');

        if (!cart || !openBtns.length || !closeBtns.length || !overlay) return;

        function openCart() {
            overlay.classList.remove('hidden');
            overlay.classList.add('flex');
            cart.classList.remove('-left-72');
            cart.classList.add('left-0');
        }

        function closeCart() {
            overlay.classList.add('hidden');
            overlay.classList.remove('flex');
            cart.classList.add('-left-72');
            cart.classList.remove('left-0');
        }

        openBtns.forEach(btn => btn.addEventListener('click', openCart));
        closeBtns.forEach(btn => btn.addEventListener('click', closeCart));
    }

    // مدیریت ساب منو
    function setupSubmenu() {
        const submenuBtn = document.querySelector('.open-submenu');
        const submenu = document.querySelector('.submenu');
        const arrow = document.querySelector('.arrow-submenu');

        if (!submenuBtn || !submenu || !arrow) return;

        submenuBtn.addEventListener('click', function () {
            submenuBtn.classList.toggle('text-green-500');
            submenu.classList.toggle('hidden');
            submenu.classList.toggle('flex');
            arrow.classList.toggle('-rotate-90');
        });
    }

    // مدیریت هشدار بالای صفحه
    function setupAlert() {
        const alert = document.querySelector('.top-alert');
        const closeBtn = document.querySelector('.close-alert-btn');

        if (!alert || !closeBtn) return;

        closeBtn.addEventListener('click', function () {
            alert.style.display = 'none';
        });
    }

    // مدیریت آکاردئون
    function setupAccordions() {
        const accordions = document.querySelectorAll('.accordion-header');

        accordions.forEach(header => {
            header.addEventListener('click', function () {
                const content = this.nextElementSibling;
                const icon = this.querySelector('svg');

                if (!content || !icon) return;

                content.classList.toggle('hidden');
                content.classList.toggle('block');
                icon.classList.toggle('rotate-90');
            });
        });
    }

    // مدیریت دکمه‌های افزایش/کاهش مقدار
    function setupQuantityInput() {
        const input = document.getElementById('customInput');
        const incrementBtn = document.querySelector('.increment');
        const decrementBtn = document.querySelector('.decrement');

        if (!input || !incrementBtn || !decrementBtn) return;

        incrementBtn.addEventListener('click', () => {
            if (input.value < 20) input.value = parseInt(input.value) + 1;
        });

        decrementBtn.addEventListener('click', () => {
            if (input.value > 1) input.value = parseInt(input.value) - 1;
        });
    }

    // مدیریت نمایش نظرات
    function setupComments() {
        const moreBtn = document.querySelector('.more-comment-btn');
        const moreText = document.querySelector('.more-comment-text');
        const moreIcon = document.querySelector('.more-comment-icon');
        const hiddenComments = document.querySelectorAll('.hidden-comment-item');

        if (!moreBtn || !moreText || !moreIcon || !hiddenComments.length) return;

        moreBtn.addEventListener('click', () => {
            hiddenComments.forEach(item => {
                item.classList.toggle('hidden');
                item.classList.toggle('block');
            });

            moreText.textContent = moreText.textContent === 'مشاهده بیشتر' ? 'مشاهده کمتر' : 'مشاهده بیشتر';

            moreIcon.classList.toggle('rotate-180');
        });
    }

    // مدیریت محدوده قیمت
    function setupPriceRange() {
        const priceElements = document.querySelectorAll(".price-input p");
        const rangeInputs = document.querySelectorAll(".range-input input");
        const range = document.querySelector(".slider-bar .progress");

        if (!priceElements.length || !rangeInputs.length || !range) return;

        const priceGap = 1000;

        function formatNumber(num) {
            return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
        }

        rangeInputs.forEach(input => {
            input.addEventListener("input", (e) => {
                let minVal = parseInt(rangeInputs[0].value) * 10;
                let maxVal = parseInt(rangeInputs[1].value) * 10;


                if (maxVal - minVal < priceGap) {
                    if (e.target.className === "min-range") {
                        rangeInputs[0].value = (maxVal - priceGap) / 10;
                    } else {
                        rangeInputs[1].value = (minVal + priceGap) / 10;
                    }
                } else {
                    priceElements[0].textContent = formatNumber(minVal);
                    priceElements[1].textContent = formatNumber(maxVal);
                    range.style.left = (rangeInputs[0].value / rangeInputs[0].max) * 100 + "%";
                    range.style.right = 100 - (rangeInputs[1].value / rangeInputs[1].max) * 100 + "%";
                }
            });
        });
    }

    // راه‌اندازی اولیه تمام کامپوننت‌ها
    function init() {
        initTheme();

        // اضافه کردن event listener برای دکمه‌های تغییر تم
        document.querySelectorAll('.toggle-theme').forEach(btn => {
            btn.addEventListener('click', toggleTheme);
        });

        setupMobileMenu();
        setupShoppingCart();
        setupSubmenu();
        setupAlert();
        setupAccordions();
        setupQuantityInput();
        setupComments();
        setupPriceRange();
    }

    // شروع اجرای کد
    init();
});