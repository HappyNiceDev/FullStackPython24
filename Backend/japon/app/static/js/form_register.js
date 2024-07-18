
const form = document.querySelector('form');


//--------------------------------------------------------------------------------------------//
//                         Envia formulario desde el js                                       //
//--------------------------------------------------------------------------------------------//

form.addEventListener('submit', function(event) {

  event.preventDefault();

  const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
  var formData = new FormData(form);

  fetch(form.action, {
      method: 'POST',
      headers: {
          'X-CSRFToken': csrfToken
      },
      body: formData,
  })
  .then(response => {
    if (response.redirected) {
        window.location.href = response.url; // Redirigir manualmente
    }
})
.catch(error => console.error('Error:', error));

/*
  .then(response => response.json())
  .then(data => {
      if (data.success) {
        // Redirigir o hacer algo si el formulario es exitoso
        console.log("Saved successfully");

      } else {
        console.log(data.errors);
              
      }
  });*/
});








/*
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
*/










