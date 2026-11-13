/* Theme: apply the saved choice before first paint, then wire up the toggle.
   The toggle button is hidden in the HTML and only shown once this runs,
   so visitors without JavaScript never see a dead, empty button. */
(function () {
  var root = document.documentElement;
  try {
    var saved = localStorage.getItem('sg-theme');
    if (saved === 'dark' || saved === 'light') root.setAttribute('data-theme', saved);
  } catch (e) {}

  function init() {
    var b = document.getElementById('themeToggle');
    if (!b) return;
    function dark() { return root.getAttribute('data-theme') === 'dark'; }
    function paint() {
      var d = dark();
      b.textContent = d ? '\u2600 Light' : '\u263E Dark';
      b.setAttribute('aria-label', d ? 'Switch to light mode' : 'Switch to dark mode');
      b.hidden = false;
    }
    b.addEventListener('click', function () {
      var n = dark() ? 'light' : 'dark';
      root.setAttribute('data-theme', n);
      try { localStorage.setItem('sg-theme', n); } catch (e) {}
      paint();
    });
    paint();
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
