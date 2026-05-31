(function () {
  const PILLARS = {
    entity: { panelId: "pillar-entity", match: ["Entities", "Entity"] },
    requirement: { panelId: "pillar-requirement", match: ["Requirements", "Requirement"] },
    change: { panelId: "pillar-change", match: ["Changes", "Change"] },
  };

  function initPillarsAccordion() {
    const root = document.getElementById("pillars-acc");
    if (!root) return;

    let active = null;

    function showPillar(key) {
      const info = PILLARS[key];
      if (!info) return;
      active = key;
      root.querySelectorAll(".pillar-panel").forEach((panel) => {
        panel.hidden = panel.id !== info.panelId;
      });
      root.querySelectorAll(".pillar-btn").forEach((btn) => {
        btn.classList.toggle("is-active", btn.dataset.pillar === key);
      });
    }

    root.querySelectorAll(".pillar-btn").forEach((btn) => {
      btn.addEventListener("click", () => showPillar(btn.dataset.pillar));
    });

    function bindOverviewClicks() {
      const overview = root.querySelector(".pillars-overview");
      if (!overview) return false;
      const svg = overview.querySelector("svg");
      if (!svg) return false;

      const nodes = svg.querySelectorAll("g.node, g.cluster");
      nodes.forEach((node) => {
        const label = (node.textContent || "").replace(/\s+/g, " ").trim();
        for (const [key, info] of Object.entries(PILLARS)) {
          if (!info.match.some((text) => label === text || label.includes(text))) continue;
          node.classList.add("pillar-clickable");
          node.style.cursor = "pointer";
          node.addEventListener("click", (event) => {
            event.preventDefault();
            showPillar(key);
          });
          break;
        }
      });
      return true;
    }

    let attempts = 0;
    const waitForDiagram = window.setInterval(() => {
      attempts += 1;
      if (bindOverviewClicks() || attempts > 40) {
        window.clearInterval(waitForDiagram);
      }
    }, 150);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initPillarsAccordion);
  } else {
    initPillarsAccordion();
  }
})();
