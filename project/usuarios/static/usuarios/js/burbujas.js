document.addEventListener('DOMContentLoaded', () => {
    const bubblesContainer = document.querySelector('.bubbles');

    function createBubble() {
        const bubble = document.createElement('span');
        bubble.classList.add('bubble');

        // tamaño aleatorio
        const size = Math.random() * 40 + 10; // entre 10 y 50px
        bubble.style.width = `${size}px`;
        bubble.style.height = `${size}px`;

        // posición horizontal aleatoria
        bubble.style.left = `${Math.random() * 100}%`;

        // duración de animación aleatoria
        bubble.style.animationDuration = `${Math.random() * 5 + 5}s`; // 5 a 10s

        bubblesContainer.appendChild(bubble);

        // remover después de la animación
        setTimeout(() => {
            bubble.remove();
        }, 10000);
    }

    // crear burbujas continuamente
    setInterval(createBubble, 400); // cada 0.4s
});
