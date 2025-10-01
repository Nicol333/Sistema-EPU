document.addEventListener('DOMContentLoaded', () => {
    // soporte para nombres antiguos (.bubbles) y nuevos en español (.burbujas)
    const bubblesContainer = document.querySelector('.burbujas, .bubbles');
    if (!bubblesContainer) {
        console.warn('No se encontró .bubbles en el DOM — revisa que el contenedor exista.');
        return;
    }

    // Asegurar que el contenedor padre (.hero) esté relativo para que las burbujas queden dentro
    const hero = bubblesContainer.closest('.seccion-principal, .hero');
    if (hero && getComputedStyle(hero).position === 'static') {
        hero.style.position = 'relative';
    }

    const rand = (min, max) => Math.random() * (max - min) + min;

    function createBubble() {
    const bubble = document.createElement('span');
    // usamos la clase en español para coincidir con CSS: .burbuja
    bubble.className = 'burbuja';

        // tamaño y posición
        const size = Math.floor(rand(12, 56));
        bubble.style.width = bubble.style.height = `${size}px`;
        bubble.style.left = `${rand(2, 98)}%`;

        // duración de subida (segundos)
        const duration = rand(6, 11);
        // establecemos la animación inline (reemplaza la propiedad CSS animation)
        bubble.style.animation = `rise ${duration}s linear forwards`;

        // variaciones visuales
        bubble.style.opacity = rand(0.35, 0.95);
        const hue = Math.floor(rand(185, 220)); // ligeros tonos azul-cian
        bubble.style.background = `radial-gradient(circle at 30% 30%, rgba(255,255,255,0.95) 0%, hsla(${hue},80%,80%,0.32) 60%, rgba(255,255,255,0.02) 100%)`;
        bubble.style.border = '1px solid rgba(255,255,255,0.35)';
        bubble.style.boxShadow = 'inset -2px -2px 6px rgba(255,255,255,0.6), inset 3px 3px 8px rgba(173,216,230,0.18), 0 3px 8px rgba(0,0,0,0.08)';
        bubble.style.pointerEvents = 'none';

        bubblesContainer.appendChild(bubble);

        // remover cuando termine la animación (con pequeño margen)
        setTimeout(() => bubble.remove(), (duration + 0.6) * 1000);
    }

    // pequeño burst inicial para que se note al cargar
    for (let i = 0; i < 6; i++) setTimeout(createBubble, i * 200);

    // generar burbujas periódicamente
    const generator = setInterval(() => {
        createBubble();
        if (Math.random() > 0.86) createBubble(); // a veces genera una extra
    }, 380);
});
