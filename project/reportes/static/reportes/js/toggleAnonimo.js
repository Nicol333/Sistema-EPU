document.addEventListener('DOMContentLoaded', function () {
    const toggleIcon = document.getElementById('toggleAnonimo');
    const hiddenInput = document.getElementById('anonimoInput');

    if (!toggleIcon || !hiddenInput) return;

    // estado: 0 = off, 1 = on
    let state = hiddenInput.value === '1' ? 1 : 0;

    function render() {
        if (state === 1) {
            toggleIcon.classList.remove('bi-toggle-off');
            toggleIcon.classList.add('bi-toggle-on');
            toggleIcon.style.color = '#00BFA5';
            hiddenInput.value = '1';
        } else {
            toggleIcon.classList.remove('bi-toggle-on');
            toggleIcon.classList.add('bi-toggle-off');
            toggleIcon.style.color = '#ffffff';
            hiddenInput.value = '0';
        }
    }

    toggleIcon.addEventListener('click', function () {
        state = state === 1 ? 0 : 1;
        render();
    });

    // permitir toggling con tecla Enter/Space cuando tenga foco
    toggleIcon.setAttribute('tabindex', '0');
    toggleIcon.addEventListener('keydown', function (e) {
        if (e.key === 'Enter' || e.key === ' ') {
            e.preventDefault();
            state = state === 1 ? 0 : 1;
            render();
        }
    });

    render();
});
