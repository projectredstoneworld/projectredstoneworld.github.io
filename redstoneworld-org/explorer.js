const projects = document.querySelectorAll("[data-project]");
let animationInProgress = false;

function nextFrame() {
  return new Promise((resolve) => {
    window.requestAnimationFrame(() => window.requestAnimationFrame(resolve));
  });
}

function cssTimeToMilliseconds(value) {
  const amount = Number.parseFloat(value);
  return value.trim().endsWith("ms") ? amount : amount * 1000;
}

function transitionBudget(element) {
  const styles = window.getComputedStyle(element);
  const durations = styles.transitionDuration.split(",").map(cssTimeToMilliseconds);
  const delays = styles.transitionDelay.split(",").map(cssTimeToMilliseconds);

  return Math.max(
    0,
    ...durations.map((duration, index) => duration + delays[index % delays.length])
  );
}

function waitForTransition(element, propertyName) {
  if (!element) return Promise.resolve();

  const budget = transitionBudget(element);
  if (budget === 0) return nextFrame();

  return new Promise((resolve) => {
    let fallbackTimer;

    function finish(event) {
      if (event && (event.target !== element || event.propertyName !== propertyName)) return;

      element.removeEventListener("transitionend", finish);
      element.removeEventListener("transitioncancel", finish);
      window.clearTimeout(fallbackTimer);
      resolve();
    }

    element.addEventListener("transitionend", finish);
    element.addEventListener("transitioncancel", finish);

    // Only used if a browser suppresses transition events unexpectedly.
    fallbackTimer = window.setTimeout(finish, budget + 100);
  });
}

function waitForSeam(project) {
  return waitForTransition(project.querySelector(".project-trigger"), "clip-path");
}

function setAccessibility(project, open) {
  const trigger = project.querySelector(".project-trigger");
  const record = project.querySelector(".project-reveal");

  trigger.setAttribute("aria-expanded", String(open));
  record.setAttribute("aria-hidden", String(!open));
  record.inert = !open;
}

async function openProject(project) {
  const record = project.querySelector(".project-reveal");

  setAccessibility(project, true);
  record.style.height = "0px";
  record.style.visibility = "visible";

  // Stage 1: flatten the shared edge over the next panel's fixed overlap.
  const seamFinished = waitForSeam(project);
  project.classList.add("is-flattening");
  await seamFinished;

  // Stage 2: keep that edge flat while opening the record.
  project.classList.add("is-open");
  project.classList.remove("is-flattening");
  await nextFrame();
  const revealFinished = waitForTransition(record, "height");
  record.style.height = `${record.scrollHeight}px`;
  await revealFinished;
  record.style.height = "auto";
}

async function closeProject(project) {
  const record = project.querySelector(".project-reveal");

  setAccessibility(project, false);
  record.style.height = `${record.getBoundingClientRect().height}px`;

  // Stage 1: close the whole record without changing the flat shared edge.
  project.classList.add("is-collapsing");
  project.classList.remove("is-open");
  await nextFrame();
  const revealFinished = waitForTransition(record, "height");
  record.style.height = "0px";
  await revealFinished;
  record.style.visibility = "hidden";

  // Stage 2: restore the diagonal, revealing the fixed overlap beneath it.
  const seamFinished = waitForSeam(project);
  project.classList.remove("is-collapsing");
  await seamFinished;
}

projects.forEach((project) => {
  const trigger = project.querySelector(".project-trigger");
  const record = project.querySelector(".project-reveal");

  project.classList.remove("is-open", "is-flattening", "is-collapsing");
  record.style.height = "0px";
  record.style.visibility = "hidden";
  record.inert = true;

  trigger.addEventListener("click", async () => {
    if (animationInProgress) return;

    const willOpen = !project.classList.contains("is-open");
    const currentlyOpen = document.querySelector("[data-project].is-open");

    animationInProgress = true;
    try {
      if (currentlyOpen) await closeProject(currentlyOpen);
      if (willOpen) await openProject(project);
    } finally {
      animationInProgress = false;
    }
  });
});
