
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
    

    var form = document.getElementById('registrationForm');
    var passwordInput = document.getElementById('password');
    var confirmPasswordInput = document.getElementById('confirm_password');
    var passwordError = document.getElementById('passwordError');
    var confirmPasswordError = document.getElementById('confirmPasswordError');

    function validatePassword() {
        var errors = [];
        var value = passwordInput.value;
        if (!/[a-z]/.test(value)) errors.push("Must contain a lowercase letter.");
        if (!/[A-Z]/.test(value)) errors.push("Must contain an uppercase letter.");
        if (!/[0-9]/.test(value)) errors.push("Must contain a digit.");
        if (!/[!@#$%^&*(),.?":{}|<>]/.test(value)) errors.push("Must contain a special character.");
        if (value.length < 8) errors.push("Must be at least 8 characters long.");

        passwordError.innerHTML = errors.join('<br>');
        if(errors.length > 0) {
            passwordError.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
        return errors.length === 0; // True if no errors
    }

    function validateConfirmPassword() {
        var errors = [];
        if (confirmPasswordInput.value !== passwordInput.value) {
            errors.push("Passwords must match.");
        }
        confirmPasswordError.innerHTML = errors.join('<br>');
        if(errors.length > 0) {
            passwordError.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
        return errors.length === 0; // True if no errors
    }

    form.addEventListener('submit', function(event) {
        var isPasswordValid = validatePassword();
        var isConfirmPasswordValid = validateConfirmPassword();
        if (!isPasswordValid || !isConfirmPasswordValid) {
            event.preventDefault(); // Stop form submission
            if (!isPasswordValid) {
                passwordError.scrollIntoView({ behavior: 'smooth', block: 'center' });
            } else if (!isConfirmPasswordValid) {
                confirmPasswordError.scrollIntoView({ behavior: 'smooth', block: 'center' });
            }
        }
    });

    passwordInput.addEventListener('input', validatePassword);
    confirmPasswordInput.addEventListener('input', validateConfirmPassword);

});


$(document).ready(function(){

    $('#submit_login').on('click', function(event) {
        event.preventDefault();
    
        const $button = $(this);
        $button.prop('disabled', true);
        const $form = $button.closest('form');
    
        const formData = $form.serialize();
    
        $.ajax({
            url: '/login',
            type: 'POST',
            data: formData,
            success: function(response) {
                if (response.success) {
                    window.location.reload();
                } else {
                    $('#login-error-message').text(response.error);
                }
                $button.prop('disabled', false);
            },
            error: function() {
                $('#login-error-message').text('An unexpected error occurred. Please try again later.');
                $button.prop('disabled', false);
            }
        });
    });
});