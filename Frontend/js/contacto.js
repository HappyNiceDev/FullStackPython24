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

var Comprobacion = false;

const Nombre = document.querySelector('input[name="nombre"]');
const Apellido = document.querySelector('input[name="apellido"]');
const Mail = document.querySelector('input[type="email"]');
const TermCond = document.querySelector('input[type="checkbox"]');
const Opcion = document.querySelector('select[name="categoria"]');


Nombre.addEventListener('blur', function () {

  if (this.value.trim() === '' || this.value.length < 3 || this.value.search(" ") != -1 || /\d/.test(this.value)) {
    this.classList.add('errorBorde');
    this.nextElementSibling.classList.add('errorAct');
    Comprobacion = false;
  } else {
    this.classList.remove('errorBorde');
    this.nextElementSibling.classList.remove('errorAct');
  }

});

Apellido.addEventListener('blur', function () {

  if (this.value.trim() === '' || this.value.length < 3 || this.value.search(" ") != -1 || /\d/.test(this.value)) {
    this.classList.add('errorBorde');
    this.nextElementSibling.classList.add('errorAct');
    Comprobacion = false;
  } else {
    this.classList.remove('errorBorde');
    this.nextElementSibling.classList.remove('errorAct');
  }

});

Mail.addEventListener('blur', function () {

  if (this.value.trim() === '' || this.value.search(" ") != -1 || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(this.value)) {
    this.classList.add('errorBorde');
    this.nextElementSibling.classList.add('errorAct');
    Comprobacion = false;
  } else {
    this.classList.remove('errorBorde');
    this.nextElementSibling.classList.remove('errorAct');
  }

});

Opcion.addEventListener('blur', function () {

  if (!this.value) {
      this.classList.add('errorBorde');
      this.nextElementSibling.classList.add('errorAct');
      Comprobacion = false;
    } else {
      this.classList.remove('errorBorde');
      this.nextElementSibling.classList.remove('errorAct');
    }

  });

TermCond.addEventListener('click', function () {

  TermCond.nextElementSibling.classList.remove('errorAct');

});

document.querySelector('form').addEventListener("submit", function (event) {

  event.preventDefault();
  Comprobacion = true;

  for (var i = 0; i < this.elements.length; i++) {
    this.elements[i].focus();
  }

  if (!Comprobacion) {
    alert("¡Complete correctamente los campos!");
    return;
  }
  else if (!TermCond.checked) {
    TermCond.nextElementSibling.classList.add('errorAct');
    alert("¡Debera aceptar los terminos y condicones!");
  } else {
    var formData = new FormData(this);
    console.log(formData)
    alert("¡Formulario enviado!");
  }

});









