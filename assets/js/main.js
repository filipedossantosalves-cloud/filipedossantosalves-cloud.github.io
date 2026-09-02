const qs = (s, root = document) => root.querySelector(s);
const qsa = (s, root = document) => [...root.querySelectorAll(s)];

const header = qs('.site-header');
const progress = qs('.scroll-progress span');
const menuToggle = qs('.menu-toggle');
const mobileMenu = qs('.mobile-menu');
const glow = qs('.cursor-glow');

let scrollFrame = 0;
const updateScrollUI = () => {
  const scrollTop = window.scrollY;
  const max = document.documentElement.scrollHeight - window.innerHeight;
  progress.style.width = `${max > 0 ? (scrollTop / max) * 100 : 0}%`;
  header.classList.toggle('scrolled', scrollTop > 20);
  scrollFrame = 0;
};
window.addEventListener('scroll', () => {
  if (!scrollFrame) scrollFrame = requestAnimationFrame(updateScrollUI);
}, { passive: true });
updateScrollUI();

let pointerFrame = 0;
document.addEventListener('pointermove', (event) => {
  if (!glow || pointerFrame) return;
  const { clientX, clientY } = event;
  pointerFrame = requestAnimationFrame(() => {
    glow.style.left = `${clientX}px`;
    glow.style.top = `${clientY}px`;
    pointerFrame = 0;
  });
});

const closeMenu = () => {
  mobileMenu?.classList.remove('open');
  menuToggle?.classList.remove('active');
  menuToggle?.setAttribute('aria-expanded', 'false');
  mobileMenu?.setAttribute('aria-hidden', 'true');
  document.body.style.overflow = '';
};

menuToggle?.addEventListener('click', () => {
  const open = !mobileMenu.classList.contains('open');
  mobileMenu.classList.toggle('open', open);
  menuToggle.classList.toggle('active', open);
  menuToggle.setAttribute('aria-expanded', String(open));
  mobileMenu.setAttribute('aria-hidden', String(!open));
  document.body.style.overflow = open ? 'hidden' : '';
});
qsa('.mobile-menu a').forEach(link => link.addEventListener('click', closeMenu));
document.addEventListener('keydown', event => {
  if (event.key === 'Escape') closeMenu();
});
window.addEventListener('resize', () => {
  if (window.innerWidth > 980) closeMenu();
}, { passive: true });

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.12, rootMargin: '0px 0px -40px' });
qsa('.reveal').forEach((element) => {
  const delay = element.dataset.delay || 0;
  element.style.setProperty('--delay', `${delay}ms`);
  observer.observe(element);
});

const isFinePointer = window.matchMedia('(pointer: fine)').matches;
if (isFinePointer && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
  qsa('[data-tilt]').forEach(card => {
    card.addEventListener('pointermove', (event) => {
      const rect = card.getBoundingClientRect();
      const x = (event.clientX - rect.left) / rect.width - 0.5;
      const y = (event.clientY - rect.top) / rect.height - 0.5;
      card.style.transform = `perspective(900px) rotateX(${-y * 5}deg) rotateY(${x * 6}deg) translateY(-2px)`;
    });
    card.addEventListener('pointerleave', () => {
      card.style.transform = '';
    });
  });

  qsa('.magnetic').forEach(button => {
    button.addEventListener('pointermove', event => {
      const rect = button.getBoundingClientRect();
      const x = event.clientX - rect.left - rect.width / 2;
      const y = event.clientY - rect.top - rect.height / 2;
      button.style.transform = `translate(${x * 0.08}px, ${y * 0.12}px)`;
    });
    button.addEventListener('pointerleave', () => button.style.transform = '');
  });
}

qs('#year').textContent = new Date().getFullYear();

// Eventos ficam prontos para Google Analytics/Tag Manager quando a conta for conectada.
window.dataLayer = window.dataLayer || [];
qsa('a[href*="wa.me"], .project-live, .project-cta, .hero-actions a').forEach((link) => {
  link.addEventListener('click', () => {
    const label = link.textContent.trim() || link.getAttribute('aria-label') || 'link';
    window.dataLayer.push({
      event: 'cta_click',
      cta_label: label,
      cta_destination: link.getAttribute('href')
    });
  });
});
