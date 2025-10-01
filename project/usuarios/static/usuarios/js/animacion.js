document.addEventListener("DOMContentLoaded", function () {
    const registerLink = document.querySelector(".register-link");
    const loginBox = document.querySelector(".login-box");

    if (registerLink && loginBox) {
        registerLink.addEventListener("click", function (e) {
            e.preventDefault();

            // Nueva animación elegante
            loginBox.classList.add("slide-fade-out");

            loginBox.addEventListener(
                "animationend",
                function () {
                    window.location.href = registerLink.getAttribute("href");
                },
                { once: true }
            );
        });
    }
});
