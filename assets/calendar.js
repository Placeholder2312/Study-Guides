/* Home-page calendar: this month and next, today highlighted, exam dates marked.
   Built from the visitor's device date, so it never needs updating by hand. */
(function () {
  var host = document.getElementById('calendar');
  if (!host) return;

  var MONTHS = ['January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'];
  // Weeks start on Monday.
  var DAYS = [['Mon', 'Monday'], ['Tue', 'Tuesday'], ['Wed', 'Wednesday'], ['Thu', 'Thursday'],
    ['Fri', 'Friday'], ['Sat', 'Saturday'], ['Sun', 'Sunday']];
  var SEMESTERS = ['I', 'II', 'III'];

  // Exam dates as YYYY-MM-DD. `sem` is the semester number (1, 2 or 3).
  // Every subject in the same semester gets the same highlight style.
  var EXAMS = [
    { date: '2026-11-17', sem: 3, name: 'Maths' },
    { date: '2026-11-19', sem: 3, name: 'DSGT' },
    { date: '2026-11-21', sem: 3, name: 'AOA' },
    { date: '2026-11-25', sem: 3, name: 'COA' },
    { date: '2026-11-27', sem: 3, name: 'OE' },
    { date: '2026-12-04', sem: 2, name: 'Maths' },
    { date: '2026-12-10', sem: 1, name: 'Physics' },
    { date: '2026-12-11', sem: 2, name: 'Physics' },
    { date: '2026-12-16', sem: 1, name: 'Mechanics' },
    { date: '2026-12-18', sem: 1, name: 'BEEE' }
  ];
  var byDate = {};
  EXAMS.forEach(function (e) {
    (byDate[e.date] = byDate[e.date] || []).push(e);
  });

  function el(tag, cls, text) {
    var n = document.createElement(tag);
    if (cls) n.className = cls;
    if (text != null) n.textContent = text;
    return n;
  }

  function iso(y, m, d) {
    return y + '-' + (m < 9 ? '0' : '') + (m + 1) + '-' + (d < 10 ? '0' : '') + d;
  }

  function buildMonth(year, month, todayKey) {
    var box = el('div', 'cal-month');
    var table = el('table', 'cal-grid');
    table.appendChild(el('caption', 'sr-only', MONTHS[month] + ' ' + year));

    var thead = el('thead');
    var headRow = el('tr');
    DAYS.forEach(function (d) {
      var th = el('th', null, d[0]);
      th.scope = 'col';
      th.abbr = d[1];
      headRow.appendChild(th);
    });
    thead.appendChild(headRow);
    table.appendChild(thead);

    var lead = (new Date(year, month, 1).getDay() + 6) % 7;
    var total = new Date(year, month + 1, 0).getDate();
    var tbody = el('tbody');
    var row = null;
    for (var i = 0; i < lead + total; i++) {
      if (i % 7 === 0) {
        row = el('tr');
        tbody.appendChild(row);
      }
      if (i < lead) {
        row.appendChild(el('td', 'pad'));
        continue;
      }
      var day = i - lead + 1;
      var dateKey = iso(year, month, day);
      var cell = el('td', 'day', day);
      cell.setAttribute('data-date', dateKey);
      if (dateKey === todayKey) {
        cell.className += ' today';
        cell.setAttribute('aria-current', 'date');
      } else if (dateKey < todayKey) {
        cell.className += ' past';
      }
      var exams = byDate[dateKey];
      if (exams) {
        cell.className += ' exam sem-' + exams[0].sem;
        cell.appendChild(el('span', 'sr-only', ', ' + exams.map(function (e) {
          return e.name + ' exam';
        }).join(', ')));
      }
      row.appendChild(cell);
    }
    while (row.children.length < 7) row.appendChild(el('td', 'pad'));
    table.appendChild(tbody);

    box.appendChild(table);
    return box;
  }

  function legendItem(cls, label) {
    var li = el('li');
    li.appendChild(el('span', 'sw ' + cls));
    li.appendChild(document.createTextNode(label));
    return li;
  }

  // Legend (what each highlight means) and the list of exams in the months shown.
  function buildKey(key, months, todayKey) {
    var shown = months.map(function (d) {
      return iso(d.getFullYear(), d.getMonth(), 1).slice(0, 7);
    });
    var list = EXAMS.filter(function (e) {
      return shown.indexOf(e.date.slice(0, 7)) !== -1;
    }).sort(function (a, b) {
      return a.date < b.date ? -1 : a.date > b.date ? 1 : 0;
    });

    key.appendChild(el('summary', null, 'Exams · ' + list.length));
    var legend = el('ul', 'cal-legend');
    legend.appendChild(legendItem('today', 'Today'));
    [1, 2, 3].forEach(function (s) {
      var used = list.some(function (e) { return e.sem === s; });
      if (used) legend.appendChild(legendItem('sem-' + s, 'Semester ' + SEMESTERS[s - 1]));
    });
    key.appendChild(legend);

    if (!list.length) return;
    var ul = el('ul', 'cal-exams');
    list.forEach(function (e) {
      var p = e.date.split('-');
      var d = new Date(+p[0], +p[1] - 1, +p[2]);
      var when = DAYS[(d.getDay() + 6) % 7][0] + ' ' + d.getDate() + ' ' + MONTHS[d.getMonth()].slice(0, 3);
      var li = el('li', e.date < todayKey ? 'past' : null);
      li.appendChild(el('span', 'sw sem-' + e.sem, d.getDate()));
      var txt = el('span');
      txt.appendChild(el('span', 'ex-name', e.name));
      txt.appendChild(el('span', 'ex-meta', (e.date < todayKey ? 'Exam done · ' : '') +
        'Semester ' + SEMESTERS[e.sem - 1] + ' · ' + when));
      li.appendChild(txt);
      ul.appendChild(li);
    });
    key.appendChild(ul);
  }

  var keyHost = document.getElementById('calendar-key');
  var renderedFor = '';
  var tapeEl = null;

  function todayKey() {
    var n = new Date();
    return iso(n.getFullYear(), n.getMonth(), n.getDate());
  }

  function render() {
    var now = new Date();
    renderedFor = todayKey();
    host.textContent = '';
    if (keyHost) keyHost.textContent = '';
    var months = [];
    var boxes = [];
    for (var m = 0; m < 2; m++) {
      var first = new Date(now.getFullYear(), now.getMonth() + m, 1);
      months.push(first);
      boxes.push(buildMonth(first.getFullYear(), first.getMonth(), renderedFor));
    }

    // One month at a time, with previous / next buttons.
    var nav = el('div', 'cal-nav');
    var prev = el('button', 'cal-btn', '‹');
    var next = el('button', 'cal-btn', '›');
    var title = el('div', 'cal-title');
    prev.type = next.type = 'button';
    prev.setAttribute('aria-label', 'Previous month');
    next.setAttribute('aria-label', 'Next month');
    title.setAttribute('aria-live', 'polite');
    function show(i) {
      boxes.forEach(function (b, j) { b.hidden = j !== i; });
      title.textContent = MONTHS[months[i].getMonth()] + ' ' + months[i].getFullYear();
      prev.disabled = i === 0;
      next.disabled = i === boxes.length - 1;
    }
    prev.addEventListener('click', function () { show(0); next.focus(); });
    next.addEventListener('click', function () { show(1); prev.focus(); });
    nav.appendChild(prev);
    nav.appendChild(title);
    nav.appendChild(next);
    host.appendChild(nav);
    boxes.forEach(function (b) { host.appendChild(b); });
    show(0);

    // Once an exam in these months is over, a strip of tape hangs off the card.
    var shownMonths = months.map(function (d) {
      return iso(d.getFullYear(), d.getMonth(), 1).slice(0, 7);
    });
    var anyDone = EXAMS.some(function (e) {
      return e.date < renderedFor && shownMonths.indexOf(e.date.slice(0, 7)) !== -1;
    });
    tapeEl = null;
    if (anyDone) {
      var tapeBox = el('div', 'cal-tape');
      tapeBox.setAttribute('aria-hidden', 'true');
      tapeEl = el('i', 'cal-tape-hang'); // the swinging strip
      tapeBox.appendChild(tapeEl);
      tapeBox.appendChild(el('i', 'cal-tape-stuck')); // the piece stuck over the card edge
      host.appendChild(tapeBox);
      angle = 0;
      spin = 60; // a small swing when the page loads
      wake();
    }

    if (keyHost) buildKey(keyHost, months, renderedFor);
  }

  // The hanging tape swings with scrolling: a damped spring pushed by scroll speed.
  // Skipped for visitors who ask for reduced motion (the strip then just hangs still).
  var animate = !(window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches);
  var angle = 0, spin = 0, flow = 0, lastY = 0, lastT = 0, lastScrollAt = 0, raf = 0;

  function step(t) {
    var dt = Math.min((t - lastT) / 1000, 0.032);
    lastT = t;
    if (dt > 0) {
      var y = window.pageYOffset;
      flow += ((y - lastY) / dt - flow) * Math.min(1, dt * 12); // smoothed scroll speed, px/s
      lastY = y;
      spin += (-0.75 * flow - 60 * angle - 5 * spin) * dt;
      angle = Math.max(-40, Math.min(40, angle + spin * dt));
    }
    if (tapeEl) tapeEl.style.transform = 'rotate(' + angle.toFixed(2) + 'deg)';
    var quiet = t - lastScrollAt > 120;
    if (!quiet || Math.abs(angle) > 0.05 || Math.abs(spin) > 0.1 || Math.abs(flow) > 1) {
      raf = requestAnimationFrame(step);
    } else {
      angle = spin = flow = 0;
      raf = 0;
      if (tapeEl) tapeEl.style.transform = '';
    }
  }

  function wake() {
    if (!animate || raf || !tapeEl) return;
    lastT = performance.now();
    lastY = window.pageYOffset;
    raf = requestAnimationFrame(step);
  }

  if (animate) {
    window.addEventListener('scroll', function () {
      lastScrollAt = performance.now();
      wake();
    }, { passive: true });
  }

  render();

  // A tab left open overnight (common on phones) redraws when it comes back into view.
  document.addEventListener('visibilitychange', function () {
    if (!document.hidden && todayKey() !== renderedFor) render();
  });
})();
