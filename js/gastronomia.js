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

const elementoTotem = document.getElementById('Totem');




// Agregar un evento click a cada imagen del totem
document.querySelectorAll('#Totem > div').forEach((imagen, index) => {

  imagen.addEventListener('click', function (event) {

    CambioClases();

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



//Se detecta click sobre alguna imagen del totem y se desencadena el cambio de las clases.
function CambioClases() {

  elementoTotem.classList.replace('TotemCentrado', 'Totem_lateral');
  elementoTotem.classList.replace('TotemCentrado', 'Totem_lateral');
  elementoTotem.style.animation = 'TotemCentradoSalida 1s ease-in-out forwards;';

  document.querySelectorAll('#Totem > div').forEach((imagen, index) => {

    let NomClass = 'Img' + (index + 1) + '_lateral';
    imagen.classList.add(NomClass);
    
  });
}


//Detecta y aplica todo los clicks aplicados a los corazones
const heartIcon = document.querySelectorAll(".like-button .heart-icon");

heartIcon.forEach(x => {

  x.addEventListener("click", () => {

    let valor = x.getAttribute('id');
    console.log(valor);
    x.classList.toggle("liked");

  });

});