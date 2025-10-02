document.addEventListener('DOMContentLoaded', function () {
    const native = document.getElementById('tipo_infraestructura');
    if (!native) return;

    // create wrapper
    const wrapper = document.createElement('div');
    wrapper.className = 'custom-select-wrapper';

    const display = document.createElement('div');
    display.className = 'custom-select';
    display.tabIndex = 0;

    const updateDisplay = () => {
        const sel = native.options[native.selectedIndex];
        display.textContent = sel ? sel.text : '';
    };

    // build options list
    const optionsBox = document.createElement('div');
    optionsBox.className = 'custom-options';

    Array.from(native.options).forEach((opt, idx) => {
        const item = document.createElement('div');
        item.className = 'custom-option';
        item.dataset.value = opt.value;
        item.textContent = opt.text;
        if (opt.disabled) item.classList.add('disabled');
        item.addEventListener('click', () => {
            if (opt.disabled) return;
            native.value = opt.value;
            updateDisplay();
            optionsBox.querySelectorAll('.custom-option').forEach(o => o.classList.remove('active'));
            item.classList.add('active');
            display.classList.remove('open');
            optionsBox.style.display = 'none';
            native.dispatchEvent(new Event('change'));
        });
        optionsBox.appendChild(item);
        if (native.selectedIndex === idx) item.classList.add('active');
    });

    display.addEventListener('click', () => {
        const isOpen = display.classList.toggle('open');
        optionsBox.style.display = isOpen ? 'block' : 'none';
    });

    // keyboard support
    display.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' || e.key === ' ') {
            e.preventDefault();
            display.click();
        }
    });

    // assemble
    wrapper.appendChild(display);
    wrapper.appendChild(optionsBox);
    native.parentNode.insertBefore(wrapper, native);
    native.classList.add('custom-select-native');

    updateDisplay();

    // close on outside click
    document.addEventListener('click', (e) => {
        if (!wrapper.contains(e.target)) {
            display.classList.remove('open');
            optionsBox.style.display = 'none';
        }
    });
});
