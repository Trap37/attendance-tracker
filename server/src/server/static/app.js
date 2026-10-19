// ── Init ──────────────────────────────────────────────────────────────────────
document.addEventListener("DOMContentLoaded", () => {
  setupTabs();
  setupOverlayDismiss();
  setupRegisterModal();
});

// ── Focus management ──────────────────────────────────────────────────────────
function anyModalOpen() {
  return [...document.querySelectorAll(".modal-overlay")].some(
    (m) => !m.classList.contains("hidden"),
  );
}

function openModal(id) {
  document.getElementById(id).classList.remove("hidden");
}

function closeModal(id) {
  document.getElementById(id).classList.add("hidden");
}

function closeAllModals() {
  document
    .querySelectorAll(".modal-overlay")
    .forEach((m) => m.classList.add("hidden"));
}

// Close modals on Escape
document.addEventListener("keydown", (e) => {
  if (e.key === "Escape") closeAllModals();
});

// Close on overlay background click
function setupOverlayDismiss() {
  document.querySelectorAll(".modal-overlay").forEach((overlay) => {
    overlay.addEventListener("click", (e) => {
      if (e.target === overlay) closeModal(overlay.id);
    });
  });
}

// Wire up [data-close] buttons
function setupModalCloseButtons() {
  document.querySelectorAll("[data-close]").forEach((btn) => {
    btn.addEventListener("click", () => closeModal(btn.dataset.close));
  });
}

// Tab Navigation
// const tabButtons = document.querySelectorAll(".tab-btn");
// const tabPanels = document.querySelectorAll(".tab-panel");

// tabButtons.forEach((button) => {
//   button.addEventListener("click", () => {
//     const selectedTab = button.dataset.tab;

//     tabButtons.forEach((tabButton) => {
//       const isActive = tabButton === button;

//       tabButton.classList.toggle("active", isActive);
//       tabButton.setAttribute("aria-selected", String(isActive));
//     });

//     tabPanels.forEach((panel) => {
//       panel.classList.toggle("hidden", panel.id !== `tab-${selectedTab}`);
//     });
//   });
// });

function setupTabs() {
  document.querySelectorAll(".tab-btn").forEach((btn) => {
    btn.addEventListener("click", () => {
      document
        .querySelectorAll(".tab-btn")
        .forEach((b) => b.classList.remove("active"));
      document
        .querySelectorAll(".tab-panel")
        .forEach((p) => p.classList.add("hidden"));
      btn.classList.add("active");
      const panel = document.getElementById(`tab-${btn.dataset.tab}`);
      if (panel) panel.classList.remove("hidden");
      if (btn.dataset.tab === "gear") {
        loadGearTab();
      } else if (btn.dataset.tab === "students") {
        loadStudents();
      } else if (btn.dataset.tab === "history") {
        loadHistory();
      } else if (btn.dataset.tab === "attendance") {
        focusScanInput();
      }
    });
  });
}

// ── Attendance scan ───────────────────────────────────────────────────────────
// async function loadAttendance() {
//   try {
//     const res = await fetch("/api/attendance/today");
//     const data = await res.json();
//     document.getElementById("attendance-count").textContent = data.count;
//   } catch {
//     // Non-critical; don't surface to user
//   }
// }

// ── Register Student modal ────────────────────────────────────────────────────
function setupRegisterModal() {
  document.getElementById("btn-register-open").addEventListener("click", () => {
    openModal("modal-register");
    document.getElementById("full_name").focus();
  });
}

// ── Gear Checkout modal ───────────────────────────────────────────────────────
function setupCheckoutModal() {
  document.getElementById("btn-checkout-open").addEventListener("click", () => {
    openModal("modal-checkout");
    document.getElementById("checkout-scan-input").focus();
  });
}

// ── Gear tab data ─────────────────────────────────────────────────────────────
