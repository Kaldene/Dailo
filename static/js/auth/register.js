const form = document.getElementById('registerForm');
const username = document.getElementById('username');
const email = document.getElementById('email');
const password = document.getElementById('password');
const passwordConfirm = document.getElementById('password2');
const errorBox = document.getElementById('errorMessage');

function validateRegisterForm(emailValue, passwordValue, passwordConfirmValue, userNameValue) {
    if (!emailValue || !passwordValue || !passwordConfirmValue || !userNameValue) {
        return "Заполните поля";
    }

    if (!isValidEmail(emailValue)) {
        return "Введите корректный email";
    }

    if (passwordValue !== passwordConfirmValue) {
        return "Пароли не совпадают";
    }

    if (passwordValue.length < 8) {
        return "Пароль должен содержать не менее 8 символов";
    }

    return "";
}

function isValidEmail(emailValue) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(emailValue);
}

document.querySelectorAll('.toggle-password').forEach(button => {
    button.addEventListener('click', () => {
        const input = document.getElementById(button.dataset.target);

        if (input.type === "password") {
            input.type = "text";
            button.innerText = "👁";
        } else {
            input.type = "password";
            button.innerText = "👁";
        }
    });
});

form.addEventListener('submit', function (e) {
    const userNameValue = username.value.trim();
    const emailValue = email.value.trim();
    const passwordValue = password.value.trim();
    const passwordConfirmValue = passwordConfirm.value.trim();

    const errorMessage = validateRegisterForm(
        emailValue,
        passwordValue,
        passwordConfirmValue,
        userNameValue
    );

    if (errorMessage) {
        e.preventDefault();
        errorBox.innerText = errorMessage;
    } else {
        errorBox.innerText = "";
    }
});