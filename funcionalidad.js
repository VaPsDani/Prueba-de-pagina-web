document.addEventListener('DOMContentLoaded', function() {
    console.log('¡JavaScript cargado y funcionando!');
});

document.getElementById('contactForm').addEventListener('submit', function(event) {
    event.preventDefault();
    alert('Formulario enviado!');
});
