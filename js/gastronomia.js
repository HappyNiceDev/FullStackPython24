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



 /* 
    document.querySelectorAll('.dropdown').forEach(function(dropdown) {
      dropdown.addEventListener('click', function(e) {
        e.stopPropagation();
        document.querySelectorAll('.nav-dropdown').forEach(function(navDropdown) {
          navDropdown.style.display = (navDropdown.style.display === 'none') ? 'block' : 'none';
        });
      });
    });
    
    document.querySelector('html').addEventListener('click', function() {
      document.querySelectorAll('.nav-dropdown').forEach(function(navDropdown) {
        navDropdown.style.display = 'none';
      });
    });
    
    document.getElementById('nav-toggle').addEventListener('click', function() {
      this.classList.toggle('active');
    });
    
    document.getElementById('nav-toggle').addEventListener('click', function() {
      document.querySelector('nav ul').style.display = (document.querySelector('nav ul').style.display === 'none') ? 'block' : 'none';
    });
  */
    


//-------------- Espera que carga todo el DOM --------------//
window.onload = function () {

  const DivContenido = document.querySelector('.Contenido');
  const elementosContenido = document.querySelectorAll('.Resumen');
  const elementoTotem = document.getElementById('Totem');
  const mediaQuery768px = window.matchMedia('(max-width: 768px)');
  var Portada = true;


  //-------------- Escucha y esjecusa solo si ya se paso la portada --------------//
  mediaQuery768px.addListener(() => !Portada && CambioClases());

  //-------------- Aplica un evento click a todos los div hijos del totem --------------//
  document.querySelectorAll('#Totem > div').forEach((imagen, index) => {
    imagen.addEventListener('click', function () {
      if(Portada){
        CambioClases();
        Portada = false
      }
      handleClickImagen(index);
    });
  });

  //-------------- Oculta o muestra los contenedores en base al evento clik sobere los divs --------------//
  function handleClickImagen(index) {
    elementosContenido.forEach((_, indice) => {
      elementosContenido[indice].classList.remove('Visible');
    });
    DivContenido.style.display = 'flex';
    elementosContenido[index].classList.add('Visible');
  }

  //-------------- Aplica cambios si hay evento clik o cambio de resolucion y segun resolucion realiza uno o otro cambio --------------//
  function CambioClases() {
    if (mediaQuery768px.matches) {
      elementoTotem.classList.replace('TotemLateral', 'TotemCentrado');
      elementoTotem.classList.replace('TotemLateral', 'TotemCentrado');
      document.querySelectorAll('#Totem > div').forEach((imagen, index) => {
        imagen.classList.remove('Img' + (index + 1) + 'Lateral');
      });
    } else {
      elementoTotem.classList.replace('TotemCentrado', 'TotemLateral');
      elementoTotem.classList.replace('TotemCentrado', 'TotemLateral');
      elementoTotem.style.animation = 'TotemCentradoSalida 1s ease-in-out forwards;';
      document.querySelectorAll('#Totem > div').forEach((imagen, index) => {
        imagen.classList.add('Img' + (index + 1) + 'Lateral');
      });
    }
  }

  //-------------- Detecta los cliks de los corazones e imprime id de la seccion --------------//
  const heartIcon = document.querySelectorAll(".like-button .heart-icon");
  heartIcon.forEach(x => {
    x.addEventListener("click", () => {
      let valor = x.getAttribute('id');
      console.log(valor);
      x.classList.toggle("liked");
    });
  });
};