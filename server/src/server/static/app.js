// ── Init ──────────────────────────────────────────────────────────────────────
document.addEventListener("DOMContentLoaded", () => {
  setupTabs();
  setupOverlayDismiss();
  setupRegisterModal();
  setupReturnModal();
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

// ── Tabs ──────────────────────────────────────────────────────────────────────
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
    });
  });
}

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

// ── Return Gear modal ─────────────────────────────────────────────────────────
function setupReturnModal() {
  document.getElementById("btn-return-submit").addEventListener("click", () => {
    openModal("modal-return");
    document.getElementById("return-scan-input").focus();
  });
}
