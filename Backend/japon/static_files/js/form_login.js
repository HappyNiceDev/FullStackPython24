

var Comprobacion = false;

const usuario = document.querySelector('input[name="usuario"]');
const pw1 = document.querySelector('input[name="pw1"]');
const pw2 = document.querySelector('input[name="pw2"]');


usuario.addEventListener('blur', function () {

  if (this.value.trim() === '' || this.value.length < 3 || this.value.search(" ") != -1 || /\d/.test(this.value)) {
    this.classList.add('errorBorde');
    this.nextElementSibling.classList.add('errorAct');
    Comprobacion = false;
  } else {
    this.classList.remove('errorBorde');
    this.nextElementSibling.classList.remove('errorAct');
  }

});

pw1.addEventListener('blur', function () {

  if (this.value.trim() === '' || this.value.length < 3 || this.value.search(" ") != -1 || /\d/.test(this.value)) {
    this.classList.add('errorBorde');
    this.nextElementSibling.classList.add('errorAct');
    Comprobacion = false;
  } else {
    this.classList.remove('errorBorde');
    this.nextElementSibling.classList.remove('errorAct');
  }

});

pw2.addEventListener('blur', function () {

  if (this.value.trim() === '' || this.value.length < 3 || this.value.search(" ") != -1 || /\d/.test(this.value)) {
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









