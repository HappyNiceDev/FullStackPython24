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