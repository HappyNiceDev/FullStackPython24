
//AQUI EMPIEZA JS DEL SLIDE
document.addEventListener("DOMContentLoaded", function() {
  var slides = document.querySelectorAll('.slider .slide');
  var radioButtons = document.querySelectorAll('input[name="grupo"]');
  var currentSlide = 0;

  // Función para mostrar el slide actual
  function showSlide(index) {
    slides.forEach(function(slide) {
      slide.classList.remove('active');
    });
    slides[index].classList.add('active');
  }

  // Función para cambiar al siguiente slide
  function nextSlide() {
    currentSlide = (currentSlide + 1) % slides.length;
    showSlide(currentSlide);
    // Selecciona el botón de radio correspondiente
    radioButtons[currentSlide].checked = true;
  }

  // Cambia al siguiente slide cada 4 segundos
  var slideInterval = setInterval(nextSlide, 4000);

  // Detiene el intervalo cuando el mouse está sobre el slider
  document.querySelector('.slider').addEventListener('mouseenter', function() {
    clearInterval(slideInterval);
  });

  // Reinicia el intervalo cuando el mouse sale del slider
  document.querySelector('.slider').addEventListener('mouseleave', function() {
    slideInterval = setInterval(nextSlide, 4000);
  });

  // Cambia al slide seleccionado por el usuario
  radioButtons.forEach(function(button, index) {
    button.addEventListener('click', function() {
      currentSlide = index;
      showSlide(currentSlide);
    });
  });
});

//AQUÍ TERMINA EL JS DEL SLIDE


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
