
document.addEventListener('DOMContentLoaded', function() {

    const openBoxButtons = document.querySelectorAll('[data-menu-target]');
    const openBoxButtonsOver = document.querySelectorAll('[data-login-button-target], [data-register-button-target]');
    const cancelBoxButtons = document.querySelectorAll('[data-cancel-button]');
    const cancelBoxButtonsOver = document.querySelectorAll('[data-cancel-button-over]');
    const overlay = document.getElementById('overlay');

    openBoxButtons.forEach(button => {
        button.addEventListener('click', () => {
            const boxSelector = button.dataset.menuTarget;
            const box = document.querySelector(boxSelector);
            openBox(box);
        });
    });

    openBoxButtonsOver.forEach(button => {
        button.addEventListener('click', () => {
            const boxSelector = button.dataset.loginButtonTarget || button.dataset.registerButtonTarget;
            const box = document.querySelector(boxSelector);
            openBoxOver(box);
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
        toggleScrollLock(true);
    }

    function openBoxOver(box) {
        if (box == null) return;
        box.classList.add('active');
    }

    function closeBox(box) {
        if (box == null) return;
        box.classList.remove('active');
        overlay.classList.remove('active');
        toggleScrollLock(false);
    }

    function closeBoxOver(box) {
        if (box == null) return;
        box.classList.remove('active');
    }

    function toggleScrollLock(isLocked) {
        const body = document.body;
    
        if (isLocked) {
            const scrollY = window.scrollY;
            body.style.position = 'fixed';
            body.style.top = `-${scrollY}px`;
            body.style.width = '100%';
        } else {
            const scrollY = body.style.top;
            body.style.position = '';
            body.style.top = '';
            window.scrollTo(0, parseInt(scrollY || '0') * -1);
        }
    }
    
});