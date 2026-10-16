    /* Contato preservado do site original no GitHub. */
    const VIENA_CONFIG = Object.freeze({
      whatsappNumber: '558192788355',
      whatsappMessage: 'Olá! Quero conversar com a Viena Studio sobre a presença digital da minha empresa.'
    });

    (() => {
      const menuButton = document.getElementById('menu-toggle');
      const mobileNav = document.getElementById('mobile-navigation');
      const menuSymbol = document.getElementById('menu-symbol');
      const dialog = document.getElementById('contact-dialog');
      let lastContactTrigger = null;

      function closeMenu(returnFocus = false) {
        mobileNav.hidden = true;
        menuButton.setAttribute('aria-expanded', 'false');
        menuButton.setAttribute('aria-label', 'Abrir menu');
        menuSymbol.setAttribute('href', '#menu');
        if (returnFocus) menuButton.focus();
      }

      menuButton.addEventListener('click', () => {
        const open = menuButton.getAttribute('aria-expanded') !== 'true';
        mobileNav.hidden = !open;
        menuButton.setAttribute('aria-expanded', String(open));
        menuButton.setAttribute('aria-label', open ? 'Fechar menu' : 'Abrir menu');
        menuSymbol.setAttribute('href', open ? '#close' : '#menu');
      });
      mobileNav.querySelectorAll('a').forEach(link => link.addEventListener('click', () => closeMenu()));
      document.addEventListener('keydown', event => {
        if (event.key === 'Escape' && !mobileNav.hidden) closeMenu(true);
      });
      document.addEventListener('click', event => {
        if (!mobileNav.hidden && !mobileNav.contains(event.target) && !menuButton.contains(event.target)) closeMenu();
      });
      document.addEventListener('focusin', event => {
        if (!mobileNav.hidden && !mobileNav.contains(event.target) && !menuButton.contains(event.target)) closeMenu();
      });
      const desktopQuery = window.matchMedia('(min-width: 1100px)');
      desktopQuery.addEventListener('change', event => { if (event.matches) closeMenu(); });

      const validPhone = /^\d{10,15}$/.test(VIENA_CONFIG.whatsappNumber);
      document.querySelectorAll('[data-preview-toggle]').forEach(button => {
        button.addEventListener('click', () => {
          const card = button.closest('.portfolio-card');
          const exploring = card.classList.toggle('is-exploring');
          button.setAttribute('aria-pressed', String(exploring));
          button.textContent = exploring ? 'Voltar ao início' : 'Explorar prévia';
        });
      });
      document.querySelectorAll('[data-whatsapp]').forEach(link => {
        if (validPhone) {
          const message = link.dataset.service
            ? `Olá! Quero conversar com a Viena Studio sobre ${link.dataset.service}.`
            : VIENA_CONFIG.whatsappMessage;
          link.href = `https://wa.me/${VIENA_CONFIG.whatsappNumber}?text=${encodeURIComponent(message)}`;
          link.target = '_blank';
          link.rel = 'noopener noreferrer';
        } else {
          link.setAttribute('aria-haspopup', 'dialog');
          link.addEventListener('click', event => {
            event.preventDefault();
            lastContactTrigger = link;
            closeMenu();
            if (typeof dialog.showModal === 'function') dialog.showModal();
            else window.alert(document.getElementById('dialog-description').textContent);
          });
        }
      });
      dialog.addEventListener('click', event => {
        if (event.target !== dialog) return;
        const bounds = dialog.getBoundingClientRect();
        if (event.clientX < bounds.left || event.clientX > bounds.right || event.clientY < bounds.top || event.clientY > bounds.bottom) dialog.close();
      });
      dialog.addEventListener('close', () => { if (lastContactTrigger) lastContactTrigger.focus(); });

      if ('IntersectionObserver' in window) {
        const links = Array.from(document.querySelectorAll('.desktop-nav .nav-link'));
        const observer = new IntersectionObserver(entries => {
          entries.forEach(entry => {
            if (!entry.isIntersecting) return;
            links.forEach(link => {
              if (link.pathname === window.location.pathname && link.hash === `#${entry.target.id}`) link.setAttribute('aria-current', 'location');
              else link.removeAttribute('aria-current');
            });
          });
        }, { rootMargin: '-18% 0px -55% 0px', threshold: 0 });
        document.querySelectorAll('main section[id]').forEach(section => observer.observe(section));
      }
      document.getElementById('year').textContent = new Date().getFullYear();

      const quickTop = document.querySelector('.quick-top');
      if (quickTop) {
        const updateQuickTop = () => quickTop.classList.toggle('is-visible', window.scrollY > 240);
        updateQuickTop();
        window.addEventListener('scroll', updateQuickTop, { passive: true });
      }
    })();

    /* One-time entrances; no animation library, scroll hijacking or hidden-content fallback. */
    (() => {
      const motionPreference = window.matchMedia('(prefers-reduced-motion: reduce)');
      if (motionPreference.matches || navigator.connection?.saveData || !('IntersectionObserver' in window) ||
          typeof Element.prototype.animate !== 'function') return;

      const activeAnimations = new Map();
      const root = document.documentElement;
      const header = document.querySelector('.site-header');
      let entranceObserver;
      let headerObserver;
      let stopped = false;

      function stopMotion() {
        stopped = true;
        root.classList.remove('has-motion');
        entranceObserver?.disconnect();
        headerObserver?.disconnect();
        activeAnimations.forEach((target, animation) => animation.cancel());
        activeAnimations.clear();
      }

      function play(target, keyframes, options) {
        if (stopped) return;
        const animation = target.animate(keyframes, {
          duration: 720, easing: 'cubic-bezier(.22,1,.36,1)', fill: 'backwards', ...options
        });
        activeAnimations.set(animation, target);
        const release = () => activeAnimations.delete(animation);
        animation.finished.then(release, release);
      }

      function splitHeading(heading) {
        const walker = document.createTreeWalker(heading, NodeFilter.SHOW_TEXT);
        const textNodes = [];
        while (walker.nextNode()) textNodes.push(walker.currentNode);
        const words = [];
        textNodes.forEach(node => {
          const fragment = document.createDocumentFragment();
          node.textContent.split(/(\s+)/u).forEach(token => {
            if (!token.trim()) { fragment.append(document.createTextNode(token)); return; }
            const word = document.createElement('span');
            word.className = 'reveal-word';
            word.textContent = token;
            fragment.append(word);
            words.push(word);
          });
          node.replaceWith(fragment);
        });
        return words;
      }

      try {
        const targets = new Map();
        document.querySelectorAll('main h1, main h2').forEach(heading => {
          targets.set(heading, { words: splitHeading(heading), delay: 0, isMainHeading: heading.tagName === 'H1' });
        });
        document.querySelectorAll(
          '.hero-badge, .hero-lead, .hero-note, .section-heading .eyebrow, ' +
          '.section-heading > p, .method-heading > p, .contact-mark, ' +
          '.contact-frame > .label, .contact-copy, .contact-caption, .section-aside, .faq-intro > p'
        ).forEach(element => targets.set(element, { delay: element.matches('.hero-lead') ? 140 : 0 }));
        ['.value-band-inner', '.pillars', '.bento-grid', '.portfolio-grid', '.timeline', '.offer-grid', '.detail-grid'].forEach(selector => {
          document.querySelectorAll(`${selector} > *`).forEach((element, index) => {
            // At most 160 ms of stagger; single-column mobile remains immediate.
            targets.set(element, { delay: window.innerWidth >= 720 ? (index % 3) * 80 : 0 });
          });
        });

        entranceObserver = new IntersectionObserver(entries => {
          try {
            entries.forEach(entry => {
              if (!entry.isIntersecting || stopped) return;
              entranceObserver.unobserve(entry.target);
              // Restored scroll positions and focused controls must stay immediately readable.
              if (entry.boundingClientRect.top < 0 || entry.target.contains(document.activeElement)) return;
              const { words, delay, isMainHeading } = targets.get(entry.target);
              if (words) {
                words.forEach((word, index) => play(word, [
                  { opacity: isMainHeading ? 1 : 0, transform: 'translateY(14px)' },
                  { opacity: 1, transform: 'translateY(0)' }
                ], { duration: 780, delay: Math.min(index * 28, 280) }));
              } else {
                play(entry.target, [
                  { opacity: 0, transform: 'translateY(18px)' },
                  { opacity: 1, transform: 'translateY(0)' }
                ], { delay });
              }
            });
          } catch { stopMotion(); }
        }, { threshold: 0.06, rootMargin: '0px 0px -24px 0px' });
        targets.forEach((config, element) => entranceObserver.observe(element));

        headerObserver = new IntersectionObserver(entries => {
          header.classList.toggle('is-scrolled', !entries[0].isIntersecting);
        });
        headerObserver.observe(document.querySelector('.hero-badge'));
        root.classList.add('has-motion');

        // Keyboard focus cancels a card entrance rather than leaving its controls faded.
        document.addEventListener('focusin', event => {
          activeAnimations.forEach((target, animation) => {
            if (target.contains(event.target)) animation.cancel();
          });
        });
        motionPreference.addEventListener('change', event => { if (event.matches) stopMotion(); });
        window.addEventListener('beforeprint', stopMotion);
        window.addEventListener('pagehide', stopMotion, { once: true });
      } catch { stopMotion(); }
    })();
