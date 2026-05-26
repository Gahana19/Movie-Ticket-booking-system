// Event listener for form submission
document.getElementById('register-form').addEventListener('submit', function (e) {
    e.preventDefault();
  
    const fullName = document.getElementById('full-name').value;
    const username = document.getElementById('username').value;
    const dob = document.getElementById('dob').value;
    const phone = document.getElementById('phone').value;
    const address = document.getElementById('address').value;
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirm-password').value;
  
    // Simple form validation
    if (password !== confirmPassword) {
      alert('Passwords do not match!');
      return;
    }
  
    if (fullName && username && dob && phone && address && password) {
      alert('Registration Successful!');
      // Here, you would send the data to your backend for registration
      // Example: sendDataToBackend(fullName, username, dob, phone, address, password);
    } else {
      alert('Please fill in all fields');
    }
  });
  
  // Mock Google login function (replace with actual OAuth logic)
  function googleLogin() {
    alert('Registering with Google...');
    // For real implementation, use Firebase or Google OAuth API here.
  }
  