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


// Obtener el contenedor principal del contenido
const contenedorContenido = document.querySelector('.Contenido');
// Obtener todos los elementos de contenido
const elementosContenido = contenedorContenido.querySelectorAll('div');


// Agregar un evento click a cada imagen del totem
document.querySelectorAll('.Totem > div').forEach((imagen, index) => {

  imagen.addEventListener('click', function (event) {

    handleClickImagen(event, index);

  });

});

// Función para manejar el clic en una imagen del totem
function handleClickImagen(event, index) {

  // Ocultar todos los elementos de contenido
  elementosContenido.forEach(elemento => {

    elemento.style.display = 'none';

  });

  contenedorContenido.style.display = 'block';

  // Mostrar el elemento de contenido correspondiente al índice de la imagen clicada
  elementosContenido[index].style.display = 'block';
}



const heartIcon = document.querySelectorAll(".like-button .heart-icon");

heartIcon.forEach(x => {

  x.addEventListener("click", () => {

    let valor = x.getAttribute('id');
    console.log(valor);
    x.classList.toggle("liked");

  });

});