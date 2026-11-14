// Sort (by year or by type) and filter (by pub_type) the list on the publications page.
// Without JavaScript the page keeps the default jekyll-scholar list grouped by year.
(function () {
  var controls = document.getElementById("pub-controls");
  var container = document.querySelector(".publications");
  if (!controls || !container) return;

  var typeOrder = controls.getAttribute("data-type-order").split(",").filter(Boolean);
  var options = Array.prototype.slice.call(controls.querySelectorAll(".pub-type-option"));
  var typeLabels = {};
  options.forEach(function (opt) {
    typeLabels[opt.getAttribute("data-pub-type")] = opt.getAttribute("data-label");
  });

  // Every paper, in the order jekyll-scholar rendered them (newest year first, file order within a year).
  var items = Array.prototype.slice.call(container.querySelectorAll("ol.bibliography > li"));

  function typeOf(li) {
    var row = li.querySelector("[data-pub-type]");
    var t = row ? row.getAttribute("data-pub-type") : "";
    return typeOrder.indexOf(t) === -1 ? "other" : t;
  }
  function yearOf(li) {
    var row = li.querySelector("[data-year]");
    return row ? parseInt(row.getAttribute("data-year"), 10) || 0 : 0;
  }
  function byYearDesc(a, b) {
    return yearOf(b) - yearOf(a);
  }

  // Only show a checkbox if at least one paper has that type.
  var counts = {};
  items.forEach(function (li) {
    var t = typeOf(li);
    counts[t] = (counts[t] || 0) + 1;
  });
  options.forEach(function (opt) {
    if (counts[opt.getAttribute("data-pub-type")]) opt.style.display = "";
  });

  function render() {
    var mode = controls.querySelector('input[name="pub-sort"]:checked').value;
    var shown = {};
    options.forEach(function (opt) {
      var cb = opt.querySelector("input");
      shown[cb.value] = cb.checked;
    });

    var groups = [];
    var byKey = {};
    function group(key, title) {
      if (!byKey[key]) {
        byKey[key] = { title: title, items: [] };
        groups.push(byKey[key]);
      }
      return byKey[key];
    }

    if (mode === "type") {
      typeOrder.concat(["other"]).forEach(function (t) {
        group(t, typeLabels[t] || t);
      });
      items.forEach(function (li) {
        group(typeOf(li)).items.push(li);
      });
      groups.forEach(function (g) {
        g.items.sort(byYearDesc);
      });
    } else {
      items
        .slice()
        .sort(byYearDesc)
        .forEach(function (li) {
          var y = String(yearOf(li));
          group(y, y).items.push(li);
        });
    }

    // Rebuild the list. Paper elements are moved, not copied, so their Abs/TLDR/Bib buttons keep working.
    container.innerHTML = "";
    groups.forEach(function (g) {
      var visible = g.items.filter(function (li) {
        return shown[typeOf(li)] !== false;
      });
      if (!visible.length) return;
      var heading = document.createElement("h2");
      heading.className = "bibliography";
      heading.textContent = g.title;
      var list = document.createElement("ol");
      list.className = "bibliography";
      visible.forEach(function (li) {
        list.appendChild(li);
      });
      container.appendChild(heading);
      container.appendChild(list);
    });
  }

  controls.addEventListener("change", render);
  controls.style.display = "";
  render();
})();
