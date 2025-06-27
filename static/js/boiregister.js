document.addEventListener("DOMContentLoaded", function () {
    const stateCityMap = {
        "Andhra Pradesh": ["Visakhapatnam", "Vijayawada", "Guntur", "Nellore"],
        "Arunachal Pradesh": ["Itanagar", "Tawang", "Pasighat", "Ziro"],
        "Assam": ["Guwahati", "Silchar", "Dibrugarh", "Jorhat"],
        "Bihar": ["Patna", "Gaya", "Bhagalpur", "Muzaffarpur"],
        "Chhattisgarh": ["Raipur", "Bilaspur", "Durg", "Korba"],
        "Goa": ["Panaji", "Margao", "Vasco da Gama", "Mapusa"],
        "Gujarat": ["Ahmedabad", "Surat", "Vadodara", "Rajkot"],
        "Haryana": ["Gurgaon", "Faridabad", "Panipat", "Ambala"],
        "Himachal Pradesh": ["Shimla", "Manali", "Dharamshala", "Solan"],
        "Jharkhand": ["Ranchi", "Jamshedpur", "Dhanbad", "Bokaro"],
        "Karnataka": ["Bengaluru", "Mysuru", "Mangaluru", "Hubli"],
        "Kerala": ["Kochi", "Thiruvananthapuram", "Kozhikode", "Thrissur","Kottayam"],
        "Madhya Pradesh": ["Bhopal", "Indore", "Jabalpur", "Gwalior"],
        "Maharashtra": ["Mumbai", "Pune", "Nagpur", "Nashik"],
        "Manipur": ["Imphal", "Thoubal", "Bishnupur"],
        "Meghalaya": ["Shillong", "Tura", "Nongpoh"],
        "Mizoram": ["Aizawl", "Lunglei", "Champhai"],
        "Nagaland": ["Kohima", "Dimapur", "Mokokchung"],
        "Odisha": ["Bhubaneswar", "Cuttack", "Rourkela", "Puri"],
        "Punjab": ["Amritsar", "Ludhiana", "Jalandhar", "Patiala"],
        "Rajasthan": ["Jaipur", "Udaipur", "Jodhpur", "Kota"],
        "Sikkim": ["Gangtok", "Namchi", "Gyalshing"],
        "Tamil Nadu": ["Chennai", "Coimbatore", "Madurai", "Salem"],
        "Telangana": ["Hyderabad", "Warangal", "Nizamabad"],
        "Tripura": ["Agartala", "Udaipur", "Dharmanagar"],
        "Uttar Pradesh": ["Lucknow", "Kanpur", "Agra", "Varanasi"],
        "Uttarakhand": ["Dehradun", "Haridwar", "Nainital", "Rudrapur"],
        "West Bengal": ["Kolkata", "Asansol", "Siliguri", "Durgapur"],
        "Andaman and Nicobar Islands": ["Port Blair"],
        "Chandigarh": ["Chandigarh"],
        "Dadra and Nagar Haveli and Daman and Diu": ["Daman", "Diu", "Silvassa"],
        "Delhi": ["New Delhi", "Dwarka", "Rohini", "Karol Bagh"],
        "Jammu and Kashmir": ["Srinagar", "Jammu", "Anantnag"],
        "Ladakh": ["Leh", "Kargil"],
        "Lakshadweep": ["Kavaratti", "Agatti"],
        "Puducherry": ["Puducherry", "Karaikal", "Mahe", "Yanam"]
    };

    const stateSelect = document.getElementById("userstate");
    const citySelect = document.getElementById("usercity");

    stateSelect.addEventListener("change", function () {
        const selectedState = this.value;
        const cities = stateCityMap[selectedState] || [];


        citySelect.innerHTML = '<option selected disabled value="">Choose...</option>';

        cities.forEach(city => {
            const option = document.createElement("option");
            option.value = city;
            option.textContent = city;
            citySelect.appendChild(option);
        });
    });
});


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
