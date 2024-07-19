//JS DE CONFIG
window.onload = function () {
    const DivContenido = document.querySelector('.informacion');
    const elementosContenido = document.querySelectorAll('.contenido-config');
    const elementosCuenta = document.querySelectorAll('.secciones-cuenta div');
    const mediaQuery768px = window.matchMedia('(max-width: 768px)');
    var Portada = true;

    //-------------- Escucha y ejecuta solo si ya se paso la portada --------------//
    mediaQuery768px.addListener(() => !Portada && CambioClases());

    //-------------- Aplica un evento click a todos los div hijos de la seccion cuenta --------------//
    elementosCuenta.forEach((elemento, index) => {
        elemento.addEventListener('click', function () {
            if (Portada) {
                CambioClases();
                Portada = false;
            }
            handleClickElemento(index);
        });
    });

    //-------------- Oculta o muestra los contenedores en base al evento click sobre los divs --------------//
    function handleClickElemento(index) {
        elementosContenido.forEach((_, indice) => {
            elementosContenido[indice].classList.remove('Visible');
        });
        DivContenido.style.display = 'flex';
        elementosContenido[index].classList.add('Visible');
    }

    //-------------- Función para cambiar clases (opcional) --------------//
    function CambioClases() {
        // Implementa la lógica necesaria para cambiar las clases si es necesario
        console.log('Cambio de clases ejecutado');
    }
};


//-----------------------drop area--------------------//

document.addEventListener('DOMContentLoaded', () => {
    const draggables = document.querySelectorAll('#draggable-aside .draggable');
    const dropArea = document.getElementById('drop-area');
    let currentDraggable = null; // Variable para mantener el elemento actualmente en el dropArea

    draggables.forEach(draggable => {
        draggable.addEventListener('dragstart', (e) => {
            e.dataTransfer.setData('text/html', draggable.outerHTML); // Guardar el HTML completo del elemento
            draggable.classList.add('dragging');
            currentDraggable = draggable; // Actualizar el elemento actual al comenzar el arrastre
        });

        draggable.addEventListener('dragend', () => {
            draggable.classList.remove('dragging');
        });
    });

    dropArea.addEventListener('dragover', (e) => {
        e.preventDefault();
        dropArea.style.backgroundColor = '#e0e0e0';  // Indicar que es un área de soltar
    });

    dropArea.addEventListener('dragleave', () => {
        dropArea.style.backgroundColor = '#fafafa';  // Restaurar el color original
    });

    dropArea.addEventListener('drop', (e) => {
        e.preventDefault();
        const data = e.dataTransfer.getData('text/html');

        // Si ya hay un elemento en el dropArea, eliminarlo antes de añadir el nuevo
        if (dropArea.querySelector('.draggable-copied')) {
            dropArea.removeChild(dropArea.querySelector('.draggable-copied'));
        }

        const newElement = document.createElement('div');
        newElement.innerHTML = data;
        newElement.classList.remove('draggable');
        newElement.classList.add('draggable-copied');

        // Añadir botón de eliminar
        const removeBtn = document.createElement('button');
        removeBtn.textContent = '×';
        removeBtn.classList.add('remove-btn');
        removeBtn.addEventListener('click', () => {
            dropArea.removeChild(newElement);
            currentDraggable = null; // Limpiar la referencia al elemento actual
            dropArea.style.backgroundColor = '#fafafa';  // Restaurar el color original
        });

        newElement.querySelector('.map-container').appendChild(removeBtn);
        dropArea.appendChild(newElement);
        dropArea.style.backgroundColor = '#fafafa';  // Restaurar el color original

        currentDraggable = newElement; // Actualizar el elemento actual al soltar en dropArea
    });
});

//-----------------------scroll aside--------------------//

document.addEventListener('DOMContentLoaded', () => {
    const aside = document.getElementById('draggable-aside');
    const scrollStep = 1; // Paso de incremento de scroll en píxeles
    let scrollInterval; // Variable para almacenar el intervalo de scroll
    let scrollingDown = true; // Variable para indicar la dirección de scroll inicial

    // Función para activar el scroll automático
    function autoScroll() {
        if (scrollingDown) {
            // Incrementar el scroll hacia abajo
            aside.scrollTop += scrollStep;
        } else {
            // Decrementar el scroll hacia arriba
            aside.scrollTop -= scrollStep;
        }

        // Verificar si se ha alcanzado el final del contenido
        if (aside.scrollTop >= aside.scrollHeight - aside.clientHeight) {
            scrollingDown = false; // Cambiar dirección a scroll hacia arriba
        } else if (aside.scrollTop <= 0) {
            scrollingDown = true; // Cambiar dirección a scroll hacia abajo
        }
    }

    // Iniciar el scroll automático
    function startAutoScroll() {
        scrollInterval = setInterval(autoScroll, 50); // Velocidad de scroll en milisegundos (50ms)
    }

    // Detener el scroll automático cuando el mouse entra en el aside
    aside.addEventListener('mouseenter', () => {
        clearInterval(scrollInterval); // Detener el scroll automático
    });

    // Reanudar el scroll automático cuando el mouse sale del aside
    aside.addEventListener('mouseleave', () => {
        startAutoScroll(); // Reanudar el scroll automático
    });

    // Iniciar el scroll automático al cargar la página
    startAutoScroll();
});


//--------------------------------------------------------------------------------------------//
//                        Constantes que ser repiten para su uso                              //
//--------------------------------------------------------------------------------------------//

const Toast = Swal.mixin({
    toast: true,
    position: "top-end",
    showConfirmButton: false,
    timer: 3000,
    timerProgressBar: true,
    didOpen: (toast) => {
        toast.onmouseenter = Swal.stopTimer;
        toast.onmouseleave = Swal.resumeTimer;
    }
});

const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

//--------------------------------------------------------------------------------------------//
//                     Configuracion auto guardado de cuenta-config                           //
//--------------------------------------------------------------------------------------------//


document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('profileForm');

    const saveField = (element) => {
        const data = new FormData(form);
        fetch(form.action, {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrfToken
            },
            body: data
        })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    Toast.fire({
                        icon: "success",
                        title: "Guardado!"
                    });
                    console.log("Saved successfully");
                } else {
                    console.log("Errors: ", data.errors);
                }
            })
            .catch(error => console.error('Error:', error));
    };

    form.querySelectorAll('input').forEach(element => {
        element.addEventListener('change', () => saveField(element));
    });
});


//--------------------------------------------------------------------------------------------//
//                                 Cambiar foto perfil                                        //
//--------------------------------------------------------------------------------------------//

const InputAction = document.getElementById('InputAction');
const FormInput = document.getElementById('FormInput');

document.getElementById('CambiaFotoPerfil').addEventListener('click', function () {
    InputAction.click();
});
document.getElementById('btn-foto').addEventListener('click', function () {
    InputAction.click();
});


FormInput.addEventListener('change', (event) => {

    // Crear el FormData
    const formData = new FormData();
    formData.append('avatar', InputAction.files[0]); // 'avatar' es el nombre del campo que esperas en el backend

    // Enviar la solicitud
    fetch('/upload-avatar/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrfToken
        },
        body: formData,
    })
        .then(response => response.json())
        .then(data => {
            if(data.success){
                location.reload();
            }
            
        })
       
});




//--------------------------------------------------------------------------------------------//
//                     Configuracion auto guardado de cuenta-config                           //
//--------------------------------------------------------------------------------------------//

form_eliminar_cuenta = document.getElementById('eliminar_cuenta')
form_eliminar_cuenta.addEventListener('submit', function (event) {
    event.preventDefault();

    Swal.fire({
        title: "Esta seguro?",
        text: "Advertencia: una vez borrada su cuenta no podra recuperar la informacion guardada.",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        cancelButtonText: "Canselar",
        confirmButtonText: "Si, borrar!"
    }).then((result) => {
        console.log(result);
        if (result.isConfirmed) {

            fetch('/eliminar_cuenta/', {
                method: 'POST',
                headers: {
                    'X-CSRFToken': form_eliminar_cuenta.querySelector('[name=csrfmiddlewaretoken]').value
                },
                body: ''
            }).then(response => {
                if (!response.ok) {
                    throw new Error('Error enviando la solicitud de borrado');
                }
                return response.json();
            }).then(data => {
                if (data.success) {
                    Swal.fire({
                        title: "Borrado!",
                        text: "Se ha eliminado su cuenta correctamente.",
                        icon: "success",
                        showConfirmButton: false,
                        timer: 5000
                    }).then((result) => {
                        window.location.href = '/'; // Redirigir manualmente
                    });
                }
            });
        }

    });
});