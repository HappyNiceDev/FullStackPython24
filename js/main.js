
document.addEventListener("DOMContentLoaded", function () { //Espera que cargue todo el html

    // Manejar clics en enlaces del menú
    var menuLinks = document.querySelectorAll(".MenuLateral a");
    menuLinks.forEach(function (link) {
        link.addEventListener("click", function (event) {
            event.preventDefault();

            // Obtener el ID de la sección objetivo del enlace
            const sectionId = this.getAttribute('href').substring(1);

            // Obtener la sección objetivo del DOM
            const targetSection = document.querySelector('.ContenidoResumido section#' + sectionId);

            // Desplazar el contenedor scrollable hasta la sección objetivo
            if (targetSection) {
                targetSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }

        });
    });

/*
    // Resaltar el elemento del menú cuando se desplaza por el contenido

    var scrollableDiv = document.querySelector('.ContenidoResumido');

    // Agregar un event listener para el evento de scroll al div scrollable
    windows.addEventListener("scroll", function () {
        // Obtener la posición de desplazamiento actual del div scrollable
        var scrollPos = scrollableDiv.scrollTop;

        // Obtener el tamaño de la ventana visible
        var windowHeight = window.innerHeight;

        // Calcular el desplazamiento equivalente al 20% de la ventana
        //var twentyPercentWindow = windowHeight * 0.2;

        // Calcular el límite superior y el límite inferior basado en el 20% de la ventana
       /var lowerLimit = scrollPos;// + twentyPercentWindow;
        var upperLimit = scrollPos + windowHeight; // - twentyPercentWindow;

        // Seleccionar todas las secciones de contenido dentro del div scrollable
        var contentSections = document.querySelectorAll(".ContenidoResumido section");

        // Iterar sobre cada sección de contenido
        contentSections.forEach(function (section) {
            // Obtener la posición superior e inferior de la sección actual
            var sectionTop = section.offsetTop;
            var sectionBottom = sectionTop + section.offsetHeight;

            // Comprobar si la posición de desplazamiento actual está dentro de los límites de la sección
            if (lowerLimit >= sectionTop && upperLimit < sectionBottom) {
                // Obtener el ID de la sección actual
                var sectionId = section.getAttribute("id");

                // Seleccionar el enlace del menú correspondiente a la sección actual
                var menuLink = document.querySelector('.MenuLateral a[href="#' + sectionId + '"]');

                // Seleccionar todos los enlaces del menú que estén resaltados
                var highlightedLinks = document.querySelectorAll(".MenuLateral a.highlight");

                // Quitar la clase de resaltado de todos los enlaces del menú
                highlightedLinks.forEach(function (link) {
                    link.classList.remove("highlight");
                });

                // Agregar la clase de resaltado al enlace del menú correspondiente a la sección actual
                menuLink.classList.add("highlight");
            }
        });
    });

*/


// Resaltar el elemento del menú cuando se desplaza por el contenido
window.addEventListener("scroll", function() {
    var scrollPos = window.scrollY;
    var contentSections = document.querySelectorAll(".ContenidoResumido section");
    var PosTopMenuLateral = document.querySelectorAll(".MenuLateral").offsetTop;
    contentSections.forEach(function(section) {
      var sectionTop = section.offsetTop;
      var AlturaMedia = section.offsetHeight - section.offsetTop
      var sectionBottom = sectionTop + section.offsetHeight;
      if (PosTopMenuLateral <= sectionTop && scrollPos < sectionBottom) {
        var sectionId = section.getAttribute("id");
        var menuLink = document.querySelector('.MenuLateral a[href="#' + sectionId + '"]');
        var highlightedLinks = document.querySelectorAll(".MenuLateral a.highlight");
        highlightedLinks.forEach(function(link) {
          link.classList.remove("highlight");
        });
        menuLink.classList.add("highlight");
      }
    });
  });






});



/*
document.addEventListener("DOMContentLoaded", function() {


    
    // Manejar clics en enlaces del menú
    var menuLinks = document.querySelectorAll(".MenuLateral a");
    menuLinks.forEach(function(link) {
      link.addEventListener("click", function(event) {
        event.preventDefault();
        var targetId = this.getAttribute("href");
        var targetElement = document.querySelector(targetId);
        var targetOffsetTop = targetElement.offsetTop;
        window.scrollTo({
          top: targetOffsetTop,
          behavior: "smooth"
        });
      });
    });
    



  
    // Resaltar el elemento del menú cuando se desplaza por el contenido
    window.addEventListener("scroll", function() {
      var scrollPos = window.scrollY;
      var contentSections = document.querySelectorAll(".content section");
      contentSections.forEach(function(section) {
        var sectionTop = section.offsetTop;
        var sectionBottom = sectionTop + section.offsetHeight;
        if (scrollPos >= sectionTop && scrollPos < sectionBottom) {
          var sectionId = section.getAttribute("id");
          var menuLink = document.querySelector('.sidebar a[href="#' + sectionId + '"]');
          var highlightedLinks = document.querySelectorAll(".sidebar a.highlight");
          highlightedLinks.forEach(function(link) {
            link.classList.remove("highlight");
          });
          menuLink.classList.add("highlight");
        }
      });
    });
  });
  
  */

   