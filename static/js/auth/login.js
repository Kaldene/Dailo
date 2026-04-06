const form = document.getElementById('loginForm');
const password = document.getElementById('password');
const email = document.getElementById('email');
const errorBox = document.getElementById('errorMessage');
const togglePassword = document.querySelector('.toggle-password');

function validateLoginForm(emailValue, passwordValue) {
    if (!emailValue || !passwordValue) {
        return "Заполните поля";
    }

    if (!isValidEmail(emailValue)) {
        return "Введите корректный email";
    }

    if (passwordValue.length < 8) {
        return "Пароль должен быть не меньше 8 символов";
    }

    return "";
}

function isValidEmail(emailValue) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(emailValue);
}

function setupPasswordToggle(input, button) {
    if (!button) return;

    button.addEventListener('click', () => {
        if (input.type === "password") {
            input.type = "text";
            button.innerText = "👁";
        } else {
            input.type = "password";
            button.innerText = "👁";
        }
    });
}

form.addEventListener('submit', function (e) {
    const emailValue = email.value.trim();
    const passwordValue = password.value.trim();

    const errorMessage = validateLoginForm(emailValue, passwordValue);

    if (errorMessage) {
        e.preventDefault();
        errorBox.innerText = errorMessage;
    } else {
        errorBox.innerText = "";
    }
});

setupPasswordToggle(password, togglePassword);