(function () {
  "use strict";

  var preloader = document.getElementById("preloader");
  if (!preloader) {
    document.body.classList.add("is-loaded");
  }

  if (preloader) {
    function hidePreloader() {
      preloader.classList.add("is-done");
      preloader.setAttribute("aria-hidden", "true");
      document.body.classList.add("is-loaded");
    }
    if (document.readyState === "complete") {
      setTimeout(hidePreloader, 400);
    } else {
      window.addEventListener("load", function () {
        setTimeout(hidePreloader, 500);
      });
      setTimeout(hidePreloader, 3500);
    }
  }

  var header = document.querySelector(".site-header");
  var menuBtn = document.querySelector(".menu-btn");
  var mobileMenu = document.querySelector(".mobile-menu");
  var menuClose = document.querySelector(".mobile-close");

  function setMenuOpen(open) {
    if (!menuBtn || !mobileMenu) return;
    menuBtn.setAttribute("aria-expanded", String(open));
    mobileMenu.classList.toggle("is-open", open);
    mobileMenu.setAttribute("aria-hidden", String(!open));
    document.body.classList.toggle("menu-open", open);
  }

  if (menuBtn) {
    menuBtn.addEventListener("click", function () {
      setMenuOpen(menuBtn.getAttribute("aria-expanded") !== "true");
    });
  }
  if (menuClose) {
    menuClose.addEventListener("click", function () {
      setMenuOpen(false);
    });
  }
  if (mobileMenu) {
    mobileMenu.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", function () {
        setMenuOpen(false);
      });
    });
  }
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") setMenuOpen(false);
  });

  function onScroll() {
    if (header) header.classList.toggle("is-scrolled", window.scrollY > 32);
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  var reveals = document.querySelectorAll(".reveal");
  if (reveals.length && "IntersectionObserver" in window) {
    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-in");
            io.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: "0px 0px -10% 0px" }
    );
    reveals.forEach(function (el) {
      io.observe(el);
    });
  } else {
    reveals.forEach(function (el) {
      el.classList.add("is-in");
    });
  }

  /* Fleet modals */
  document.querySelectorAll("[data-modal]").forEach(function (trigger) {
    trigger.addEventListener("click", function (e) {
      e.preventDefault();
      var id = trigger.getAttribute("data-modal");
      var modal = document.getElementById(id);
      if (modal) {
        modal.classList.add("is-open");
        modal.setAttribute("aria-hidden", "false");
        document.body.classList.add("menu-open");
      }
    });
  });

  document.querySelectorAll(".modal").forEach(function (modal) {
    var closeBtn = modal.querySelector(".modal-close");
    function closeModal() {
      modal.classList.remove("is-open");
      modal.setAttribute("aria-hidden", "true");
      if (!mobileMenu || !mobileMenu.classList.contains("is-open")) {
        document.body.classList.remove("menu-open");
      }
    }
    if (closeBtn) closeBtn.addEventListener("click", closeModal);
    modal.addEventListener("click", function (e) {
      if (e.target === modal) closeModal();
    });
  });

  /* Contact form */
  document.querySelectorAll(".quote-form").forEach(function (form) {
    var success = form.parentElement
      ? form.parentElement.querySelector(".form-success")
      : document.querySelector(".form-success");
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var valid = true;
      form.querySelectorAll("[required]").forEach(function (field) {
        field.classList.remove("error");
        if (!field.value.trim()) {
          field.classList.add("error");
          valid = false;
        }
      });
      var email = form.querySelector('[name="email"]');
      if (email && email.value && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value)) {
        email.classList.add("error");
        valid = false;
      }
      if (!valid) return;
      if (success) success.classList.add("is-visible");
      form.reset();
      var btn = form.querySelector('button[type="submit"]');
      if (btn) {
        var t = btn.textContent;
        btn.textContent = "Submitted";
        btn.disabled = true;
        setTimeout(function () {
          btn.textContent = t;
          btn.disabled = false;
        }, 4000);
      }
    });
  });
})();
