// Interactive star rating for static .stars elements
(function () {
    function renderStars(el) {
        var initial = 0;
        var dataInit = el.getAttribute('data-initial');
        if (dataInit) { initial = Math.round(parseFloat(dataInit)); }
        else {
            var text = (el.textContent || '').trim();
            for (var i = 0; i < text.length; i++) { if (text[i] === '★') initial++; else break; }
        }
        var noAnim = el.classList.contains('no-anim');
        el.dataset.rating = initial;
        el.innerHTML = '';
        for (var i = 1; i <= 5; i++) {
            var span = document.createElement('span');
            span.className = 'star' + (i <= initial ? ' filled' : '');
            // make non-interactive if noAnim is true
            span.tabIndex = noAnim ? -1 : 0;
            span.setAttribute('data-value', i);
            span.innerText = '★';
            el.appendChild(span);
        }

        var stars = el.querySelectorAll('.star');

        function setVisual(r) {
            el.dataset.rating = r;
            stars.forEach(function (s) {
                var v = parseInt(s.getAttribute('data-value'));
                if (v <= r) s.classList.add('filled'); else s.classList.remove('filled');
            });
        }

        stars.forEach(function (s) {
            if (!noAnim) {
                s.addEventListener('mouseover', function () {
                    var v = parseInt(this.getAttribute('data-value'));
                    stars.forEach(function (s2) {
                        var vv = parseInt(s2.getAttribute('data-value'));
                        if (vv <= v) s2.classList.add('hover'); else s2.classList.remove('hover');
                    });
                });
                s.addEventListener('mouseout', function () {
                    stars.forEach(function (s2) { s2.classList.remove('hover'); });
                });

                s.addEventListener('click', function () {
                    var v = parseInt(this.getAttribute('data-value'));
                    setVisual(v);
                    // Placeholder: send to server if desired
                    console.log('Rated', v, 'for element', el);
                    // show selection value in adjacent .avg element (create if missing)
                    var info = el.closest('.report-info');
                    if (info) {
                        var avgEl = info.querySelector('.avg');
                        if (!avgEl) {
                            avgEl = document.createElement('div');
                            avgEl.className = 'avg';
                            info.appendChild(avgEl);
                        }
                        avgEl.textContent = v + '/5';
                        avgEl.classList.add('user-selected');
                    }
                });
                s.addEventListener('keydown', function (e) {
                    if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); this.click(); }
                    if (e.key === 'ArrowLeft' || e.key === 'ArrowDown') {
                        var cur = parseInt(el.dataset.rating) || 0; if (cur > 1) setVisual(cur - 1);
                    }
                    if (e.key === 'ArrowRight' || e.key === 'ArrowUp') {
                        var cur = parseInt(el.dataset.rating) || 0; if (cur < 5) setVisual(cur + 1);
                    }
                });
            }
        });
    }

    document.addEventListener('DOMContentLoaded', function () {
        var lists = document.querySelectorAll('.stars');
        lists.forEach(function (el) { renderStars(el); });
    });
})();
