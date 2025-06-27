document.addEventListener('DOMContentLoaded', function () {
  console.log("Validation script running...");

  const form = document.querySelector('.needs-validation');
  const submitButton = document.querySelector('button[type="submit"]');

  form.addEventListener('submit', function (event) {
    if (!form.checkValidity()) {
      event.preventDefault();
      event.stopPropagation();
      form.classList.add('was-validated');
      console.log("Form is invalid.");
    } else {
    form.submit();
    }
  });
});