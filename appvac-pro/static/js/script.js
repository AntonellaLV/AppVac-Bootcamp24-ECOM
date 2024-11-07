document.addEventListener('DOMContentLoaded', function() {
    console.log('JavaScript cargado correctamente.');
});

document.addEventListener('DOMContentLoaded', function() {
    const toggleButton = document.querySelector('.navbar-toggler');
    const navbarCollapse = document.querySelector('#navbarNav');

    toggleButton.addEventListener('click', function() {
        navbarCollapse.classList.toggle('show');
    });
});

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();

        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});
