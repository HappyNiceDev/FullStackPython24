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


//-----------------------editor de texto--------------------//
ClassicEditor
        .create(document.querySelector('#editor'))
        .catch(error => {
            console.error(error);
        });



 
