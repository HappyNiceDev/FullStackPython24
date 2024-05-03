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


document.addEventListener("DOMContentLoaded", function () { //Espera que cargue todo el html
const dd = document.documentElement;



  // Manejar clics en enlaces del menú
  var menuLinks = dd.querySelectorAll(".MenuLateral a");
  menuLinks.forEach(function (link) {
    link.addEventListener("click", function (event) {
      event.preventDefault();

      // Obtener el ID de la sección objetivo del enlace
      const sectionId = this.getAttribute('href').substring(1);

      // Obtener la sección objetivo del DOM
      const targetSection = dd.querySelector('.ContenidoResumido section#' + sectionId);

      // Desplazar el contenedor scrollable hasta la sección objetivo
      if (targetSection) {
        targetSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }

    });
  });


  // Resaltar el elemento del menú cuando se desplaza por el contenido
  window.addEventListener("scroll", function () {

    dd.querySelectorAll(".ResumenTematico section").forEach(function (section) {
      var sectionTop = section.getBoundingClientRect().top;
    
      if (sectionTop <= 150) {
        var sectionId = section.getAttribute("id");
        var menuLink = document.querySelector('.MenuLateral a[href="#' + sectionId + '"]');

        document.querySelectorAll(".MenuLateral a.highlight").forEach(function (link) {
          link.classList.remove("highlight");
        });

        menuLink.classList.add("highlight");
      }

    });

  });


});
