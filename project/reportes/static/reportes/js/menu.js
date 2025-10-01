// static/js/menu.js
document.addEventListener('DOMContentLoaded', () => {
    const menuBtn = document.querySelector('.menu-btn');
    const sideMenu = document.getElementById('side-menu');

    if (menuBtn && sideMenu) {
        menuBtn.addEventListener('click', () => {
            sideMenu.classList.toggle('active');
        });
    }
});
