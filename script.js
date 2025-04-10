const navLinks = document.querySelectorAll(".nav-links a");

navLinks.forEach(link => {
  link.addEventListener("click", () => {
    navLinks.forEach(l => l.classList.remove("active"));
    link.classList.add("active");
  });
});

document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("appointment-form");
    const feedback = document.getElementById("form-feedback");
  
    form.addEventListener("submit", function(event) {
      event.preventDefault(); // Prevent the form from refreshing the page
  
      // Get the form values
      const firstName = document.getElementById("first-name").value.trim();
      const lastName = document.getElementById("last-name").value.trim();
      const phone = document.getElementById("phone").value.trim();
      const email = document.getElementById("email").value.trim();
  
      // Validate the inputs
      if (firstName && lastName && phone && email) {
        // Show a success message
        feedback.style.display = "block";
        feedback.textContent = "Your appointment has been scheduled successfully!";
        feedback.style.color = "green";
        
        // Reset the form
        form.reset();
      } else {
        // Show an error message
        feedback.style.display = "block";
        feedback.textContent = "Please fill out all fields correctly.";
        feedback.style.color = "red";
      }
    });
  });
  