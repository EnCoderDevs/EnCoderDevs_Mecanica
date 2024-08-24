function mostrarFormulario(formulario) {
    
    const formularios = document.querySelectorAll('form');
    
    formularios.forEach(form => form.classList.add('hidden'));

  
    const formSeleccionado = document.getElementById(`${formulario}-form`);
    formSeleccionado.classList.remove('hidden');
}


document.addEventListener("DOMContentLoaded", function() {

    const formularios = document.querySelectorAll('form');
    formularios.forEach(form => form.classList.add('hidden'));
});

document.addEventListener('DOMContentLoaded', function() {
    const buttons = document.querySelectorAll('.product button');

    buttons.forEach(button => {
        button.addEventListener('click', function() {
            alert('Product added to cart!');
        });
    });
});
