document.addEventListener('DOMContentLoaded', function () {
  const toggle = document.getElementById('darkModeToggle');
  const body = document.body;

  function updateIcon(isDark) {
    if (toggle) {
      toggle.textContent = isDark ? '☀️' : '🌙';
      toggle.setAttribute('aria-label', isDark ? 'Switch to light mode' : 'Switch to dark mode');
    }
  }

  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  const storedPreference = localStorage.getItem('dark-mode');

  let isDark = storedPreference === 'enabled' ? true
             : storedPreference === 'disabled' ? false
             : prefersDark;

  body.classList.toggle('dark-mode', isDark);
  updateIcon(isDark);

  if (toggle) {
    toggle.addEventListener('click', () => {
      isDark = !isDark;
      body.classList.toggle('dark-mode', isDark);
      localStorage.setItem('dark-mode', isDark ? 'enabled' : 'disabled');
      updateIcon(isDark);
    });
  }

  setTimeout(() => body.classList.add('transition'), 100);
});


$(document).ready(function () {
  $('#skillCarousel').carousel();
});
