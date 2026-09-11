const projects = document.querySelectorAll("[data-project]");

function setProjectState(project, open) {
  const trigger = project.querySelector(".project-trigger");
  const record = project.querySelector(".project-reveal");

  project.classList.toggle("is-open", open);
  trigger.setAttribute("aria-expanded", String(open));
  record.setAttribute("aria-hidden", String(!open));
  record.inert = !open;
}

projects.forEach((project) => {
  const trigger = project.querySelector(".project-trigger");
  const record = project.querySelector(".project-reveal");

  record.inert = true;

  trigger.addEventListener("click", () => {
    const willOpen = !project.classList.contains("is-open");

    projects.forEach((candidate) => setProjectState(candidate, false));
    if (willOpen) setProjectState(project, true);
  });
});
