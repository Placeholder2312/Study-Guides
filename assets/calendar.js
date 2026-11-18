/* Home-page calendar: this month and next, today highlighted.
   Built from the visitor's device date, so it never needs updating by hand. */
(function () {
  var host = document.getElementById('calendar');
  if (!host) return;

  var MONTHS = ['January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'];
  // Weeks start on Monday.
  var DAYS = [['Mon', 'Monday'], ['Tue', 'Tuesday'], ['Wed', 'Wednesday'], ['Thu', 'Thursday'],
    ['Fri', 'Friday'], ['Sat', 'Saturday'], ['Sun', 'Sunday']];

  function el(tag, cls, text) {
    var n = document.createElement(tag);
    if (cls) n.className = cls;
    if (text != null) n.textContent = text;
    return n;
  }

  function iso(y, m, d) {
    return y + '-' + (m < 9 ? '0' : '') + (m + 1) + '-' + (d < 10 ? '0' : '') + d;
  }

  function buildMonth(year, month, now) {
    var box = el('div', 'cal-month');
    var table = el('table', 'cal-grid');
    table.appendChild(el('caption', null, MONTHS[month] + ' ' + year));

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
      var cell = el('td', 'day', day);
      cell.setAttribute('data-date', iso(year, month, day));
      if (year === now.getFullYear() && month === now.getMonth() && day === now.getDate()) {
        cell.className += ' today';
        cell.setAttribute('aria-current', 'date');
      }
      row.appendChild(cell);
    }
    while (row.children.length < 7) row.appendChild(el('td', 'pad'));
    table.appendChild(tbody);

    box.appendChild(table);
    return box;
  }

  var now = new Date();
  for (var m = 0; m < 2; m++) {
    var first = new Date(now.getFullYear(), now.getMonth() + m, 1);
    host.appendChild(buildMonth(first.getFullYear(), first.getMonth(), now));
  }
})();
