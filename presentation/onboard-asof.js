const slides = Array.from(document.querySelectorAll(".slide"));
const currentSlide = document.getElementById("current-slide");
const totalSlides = document.getElementById("total-slides");

let activeIndex = 0;

function formatIndex(index) {
  return String(index + 1).padStart(2, "0");
}

function updateProgress(index) {
  activeIndex = index;
  currentSlide.textContent = formatIndex(index);
  totalSlides.textContent = String(slides.length).padStart(2, "0");
}

function goToSlide(index) {
  const bounded = Math.max(0, Math.min(index, slides.length - 1));
  slides[bounded].scrollIntoView({ behavior: "smooth", block: "start" });
  updateProgress(bounded);
}

document.addEventListener("keydown", (event) => {
  if (event.key === "ArrowRight" || event.key === "PageDown") {
    event.preventDefault();
    goToSlide(activeIndex + 1);
  }

  if (event.key === "ArrowLeft" || event.key === "PageUp") {
    event.preventDefault();
    goToSlide(activeIndex - 1);
  }
});

document.querySelector('[data-action="prev"]').addEventListener("click", () => {
  goToSlide(activeIndex - 1);
});

document.querySelector('[data-action="next"]').addEventListener("click", () => {
  goToSlide(activeIndex + 1);
});

document.querySelector('[data-action="print"]').addEventListener("click", () => {
  window.print();
});

const observer = new IntersectionObserver(
  (entries) => {
    const visible = entries
      .filter((entry) => entry.isIntersecting)
      .sort((a, b) => b.intersectionRatio - a.intersectionRatio)[0];

    if (!visible) return;
    const index = slides.indexOf(visible.target);
    if (index >= 0) updateProgress(index);
  },
  { threshold: [0.4, 0.75] },
);

slides.forEach((slide) => observer.observe(slide));
updateProgress(0);
