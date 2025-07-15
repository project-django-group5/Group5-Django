document.addEventListener('DOMContentLoaded', function () {
  const toggle = document.getElementById('darkModeToggle');
  const body = document.body;

  function updateIcon(isDark) {
    if (toggle) {
      toggle.textContent = isDark ? '☀️' : '🌙';
    }
  }

  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  let storedPreference = localStorage.getItem('dark-mode');
  let isDark = false;

  if (storedPreference === 'enabled') {
    isDark = true;
  } else if (storedPreference === 'disabled') {
    isDark = false;
  } else {
    isDark = prefersDark;
  }

  body.classList.toggle('dark-mode', isDark);
  updateIcon(isDark);

  if (toggle) {
    toggle.addEventListener('click', () => {
      isDark = !body.classList.contains('dark-mode');
      body.classList.toggle('dark-mode', isDark);
      localStorage.setItem('dark-mode', isDark ? 'enabled' : 'disabled');
      updateIcon(isDark);
    });
  }
});
