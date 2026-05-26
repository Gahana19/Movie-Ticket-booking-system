document.getElementById('login-form').addEventListener('submit', function (e) {
    e.preventDefault();
  
    // Get the values from the form fields
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
  
    // Simple validation
    if (username && password) {
      alert('Login Successful');
      // Here you would typically send the data to the backend
      // Example: sendDataToBackend(username, password);
    } else {
      alert('Please fill in all fields');
    }
  });
  
  // Mock Google login function (can be replaced with actual OAuth logic)
  function googleLogin() {
    alert('Logging in with Google...');
    // For real implementation, integrate with Firebase or Google OAuth
  }
  