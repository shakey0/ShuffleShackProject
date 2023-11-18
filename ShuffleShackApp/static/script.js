
document.addEventListener('DOMContentLoaded', function() {

    const openBoxButtons = document.querySelectorAll('[data-menu-target], [data-login-button-target], [data-register-button-target]');
    const cancelBoxButtons = document.querySelectorAll('[data-cancel-button]');
    const cancelBoxButtonsOver = document.querySelectorAll('[data-cancel-button-over]');
    const overlay = document.getElementById('overlay');

    openBoxButtons.forEach(button => {
        button.addEventListener('click', () => {
            const boxSelector = button.dataset.menuTarget || button.dataset.loginButtonTarget || button.dataset.registerButtonTarget;
            const box = document.querySelector(boxSelector);
            openBox(box);
        });
    });

    overlay.addEventListener('click', () => {
        const activeOverBox = document.querySelector('.login-box.active, .register-box.active');
        if (!activeOverBox) {
            const boxes = document.querySelectorAll('.main-menu-box-unauth.active, .main-menu-box-auth.active');
            boxes.forEach(box => {
                closeBox(box);
            });
        }
    });

    cancelBoxButtons.forEach(button => {
        button.addEventListener('click', () => {
            const box = button.closest('.main-menu-box-unauth, .main-menu-box-auth');
            closeBox(box);
        });
    });

    cancelBoxButtonsOver.forEach(button => {
        button.addEventListener('click', () => {
            const box = button.closest('.login-box, .register-box');
            closeBoxOver(box);
        });
    });

    function openBox(box) {
        if (box == null) return;
        box.classList.add('active');
        overlay.classList.add('active');
    }

    function closeBox(box) {
        if (box == null) return;
        box.classList.remove('active');
        overlay.classList.remove('active');
    }

    function closeBoxOver(box) {
        if (box == null) return;
        box.classList.remove('active');
    }

});