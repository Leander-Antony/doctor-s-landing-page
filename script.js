const navLinks = document.querySelectorAll(".nav-links a");

navLinks.forEach(link => {
  link.addEventListener("click", () => {
    navLinks.forEach(l => l.classList.remove("active")); // Remove 'active' from all
    link.classList.add("active"); // Add 'active' to clicked link
  });
});
