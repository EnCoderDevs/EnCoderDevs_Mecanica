// scripts.js

function mostrarFormulario(formulario) {
    // Obtener todos los formularios
    const formularios = document.querySelectorAll('form');
    // Ocultar todos los formularios
    formularios.forEach(form => form.classList.add('hidden'));

    // Mostrar el formulario seleccionado
    const formSeleccionado = document.getElementById(`${formulario}-form`);
    formSeleccionado.classList.remove('hidden');
}

// Asegúrate de que el script se cargue después del DOM
document.addEventListener("DOMContentLoaded", function() {
    // Inicialmente, ocultar todos los formularios
    const formularios = document.querySelectorAll('form');
    formularios.forEach(form => form.classList.add('hidden'));
});
