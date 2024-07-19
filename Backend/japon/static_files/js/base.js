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


// Función para ejecutar código solo si el elemento existe
function executeIfElementExists(selector, callback) {
  const element = document.querySelector(selector);
  if (element) {
    callback(element);
  }
}
/*
function executeIfElementExists2(selector2, callback2) {
  const element2 = document.querySelector(selector2);
  if (element2) {
    callback2(element2);
  }
}*/

//--------------------------------------------------------------------------------------------//
//                              Abre SweetAlert2 - LOGIN                                      //
//--------------------------------------------------------------------------------------------//

executeIfElementExists('#login', boton => {
  boton.addEventListener('click', function (event) {
    event.preventDefault();

    fetch('/login/')
      .then(response => response.text())
      .then(html => {
        Swal.fire({
          title: 'Iniciar sesion',
          html: html,
          showCancelButton: false,
          focusConfirm: true,
          preConfirm: () => {
            const form = document.getElementById('Form');
            const formData = new FormData(form);

            return fetch('/login/', {
              method: 'POST',
              body: formData,
              headers: {
                'X-CSRFToken': form.querySelector('[name=csrfmiddlewaretoken]').value
              }
            }).then(response => {
              //console.log(response.mensaje);
              if (!response.ok) {
                throw new Error('Error en el envío del formulario');
              }
              return response.json();
            }).then(data => {
              if (data.success) {
                Swal.fire({
                  title: data.mensaje,
                  icon: 'success',
                  showConfirmButton: false,
                  timer: 2000
                }).then((result) => {
                  window.location.href = '/'; // Redirigir manualmente
                });
              } else {
                Swal.fire({
                  title: 'Algo salio mal!',
                  text: 'Por favor vuelva a intentar',
                  icon: 'error'
                });
              }
              //Swal.showValidationMessage(`Error: ${error}`);
            });
          }
        });
      })
      .catch(error => {
        console.error('Error:', error);
        Swal.fire('Error', 'No se pudo cargar el formulario.', 'error');
      });
  });
});


//--------------------------------------------------------------------------------------------//
//                              Abre SweetAlert2 - REGISTER                                      //
//--------------------------------------------------------------------------------------------//

executeIfElementExists('#registrar', boton => {
  boton.addEventListener('click', function (event) {
    event.preventDefault();

    fetch('/register/')
      .then(response => response.text())
      .then(html => {
        Swal.fire({
          title: 'Registrar una nueva cuenta',
          html: html,
          showCancelButton: false,
          focusConfirm: true,
          preConfirm: () => {
            const form = document.getElementById('Form');
            const formData = new FormData(form);

            return fetch('/register/', {
              method: 'POST',
              body: formData,
              headers: {
                'X-CSRFToken': form.querySelector('[name=csrfmiddlewaretoken]').value
              }
            }).then(response => {
              //console.log(response.mensaje);
              if (!response.ok) {
                throw new Error('Error en el envío del formulario');
              }
              return response.json();
            }).then(data => {
              if (data.success) {
                Swal.fire({
                  title: data.mensaje,
                  icon: 'success',
                  showConfirmButton: false,
                  timer: 4000
                }).then((result) => {
                  window.location.href = '/'; // Redirigir manualmente
                });
              } else {
                Swal.fire({
                  title: 'Algo salio mal!',
                  text: 'Por favor vuelva a intentar',
                  icon: 'error'
                });
              }
              Swal.showValidationMessage(`Error: ${error}`);
            });
          }
        });
      })
      .catch(error => {
        console.error('Error:', error);
        Swal.fire('Error', 'No se pudo cargar el formulario.', 'error');
      });
  });
});



/*
fetch('/login/')
.then(response => response.text())
.then(html => {
    Swal.fire({
        title: 'Formulario',
        html: html,
        showCancelButton: true,
        focusConfirm: false,
        preConfirm: () => {
            return new Promise((resolve) => {
                resolve({
                    form: document.getElementById('Form')
                });
            });
        }
    }).then((result) => {
        if (result.isConfirmed) {
            document.getElementById('Form').submit();
        }
    });
})
.catch(error => {
    console.error('Error:', error);
    Swal.fire('Error', 'No se pudo cargar el formulario.', 'error');
});


//AQUÍ TERMINA EL JS DEL NAV BAR
/*
document.addEventListener('DOMContentLoaded', function() {
fetch('/')
    .then(response => response.json())
    .then(data => {
        const myVariable = data.message;
        console.log('Variable de sesión:', myVariable);
        // Otras acciones con myVariable
    });
});*/
/*
function registrado(){
  var djangoUsername = "x"; //document.getElementById('djangoUsername').value
  Swal.fire({
    position: "center",
    icon: "success",
    title: "Bienvenido " + djangoUsername + " se a registrado corectamente",
    showConfirmButton: false,
    timer: 4000
  });
}*/