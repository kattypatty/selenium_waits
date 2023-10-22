document.addEventListener("DOMContentLoaded", function() {
  setTimeout(function() {
    document.getElementById('startTest').classList.remove('hidden');
  }, 5000);

  document.getElementById('startTest').addEventListener('click', function() {
    document.getElementById('registrationForm').classList.remove('hidden');
  });

  document.getElementById('register').addEventListener('click', function() {
    const login = document.getElementById('login').value;
    const password = document.getElementById('password').value;
    const agree = document.getElementById('agree').checked;

    if (login && password && agree) {
      document.getElementById('registrationForm').classList.add('hidden');
      const loader = document.getElementById('loader');
      loader.classList.remove('hidden');

      setTimeout(function() {
        loader.classList.add('hidden');
        document.getElementById('successMessage').classList.remove('hidden');
      }, 3000);
    } else {
      alert('Пожалуйста, заполните все поля и согласитесь с правилами.');
    }
  });
});

  
  
