//AQUÍ EMPIEZA EL JS DEL NAV BAR
$('.dropdown').click(function (e) {
  e.stopPropagation();
  $('.nav-dropdown').toggle();
});

$('html').click(function () {
  $('.nav-dropdown').hide();
})

$('#nav-toggle').on('click', function () {
  this.classList.toggle('active');
});

$("#nav-toggle").click(function () {
  $("nav ul").toggle();
});

//AQUÍ TERMINA EL JS DEL NAV BAR




// Obtener todas las imágenes del totem
const imagenesTotem = document.querySelectorAll('.Totem > div');

// Obtener el contenedor principal del contenido
const contenedorContenido = document.querySelector('.Contenido');

// Función para manejar el clic en una imagen del totem
function handleClickImagen(event) {
  // Obtener el índice de la imagen clicada
  const indice = Array.from(imagenesTotem).indexOf(event.target);

  // Obtener todos los elementos de contenido
  const elementosContenido = contenedorContenido.querySelectorAll('div');

  // Ocultar todos los elementos de contenido
  elementosContenido.forEach(elemento => {
    elemento.style.display = 'none';
  });

  // Mostrar el elemento de contenido correspondiente al índice de la imagen clicada
  elementosContenido[indice].style.display = 'block';
}

// Agregar un evento click a cada imagen del totem
imagenesTotem.forEach(imagen => {
  imagen.addEventListener('click', handleClickImagen);
});
