document.addEventListener('DOMContentLoaded', function() {
  const forms = document.querySelectorAll('.needs-validation');

  forms.forEach(function(form) {
    form.addEventListener('submit', function(event) {
      event.preventDefault();
      event.stopPropagation();

      const passwordInput = form.querySelector('#password');
      const retypeInput = form.querySelector('#retypepassword');
      const checkboxInput = form.querySelector('#gridCheck'); // checkbox input

      const password = passwordInput.value.trim();
      const retypePassword = retypeInput.value.trim();

      const passwordPattern = /^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+\-=[\]{};':"\\|,.<>\/?~`]).{8,}$/;

      // Reset previous custom validity
      passwordInput.setCustomValidity('');
      retypeInput.setCustomValidity('');
      checkboxInput.setCustomValidity('');

      // Validate password strength
      if (!passwordPattern.test(password)) {
        passwordInput.setCustomValidity('Password must have at least 8 characters, including one uppercase letter, one digit, and one special symbol.');
      }

      // Validate password match
      if (password !== retypePassword) {
        retypeInput.setCustomValidity('Passwords do not match!');
      }

      if (!checkboxInput.checked) {
        checkboxInput.setCustomValidity('You must agree to the terms.');
      }

      passwordInput.nextElementSibling.textContent = passwordInput.validationMessage;
      retypeInput.nextElementSibling.textContent = retypeInput.validationMessage;


      form.classList.add('was-validated');

      // Submit form if all valid
      if (form.checkValidity()) {
        form.submit();
      }
    });
  });
});
