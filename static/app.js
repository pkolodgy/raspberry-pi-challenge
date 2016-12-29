$(document).ready(function() {


  $('header').on('submit', '#fruit-search', function(e){
    e.preventDefault();
    $('main').children().remove()
    var fruit = $("input[name='fruit_name']").val()
    $.ajax({
      method: $(e.target).attr('method'),
      url: '/'+fruit+'/pie'
    })
    .done(function(r) {
      $('main').append(r)
      $('.recipe-body').hide()
      $(e.target)[0].reset()
    })
  })

  $('main').on('click', '.recipe-header', function(e) {
    e.preventDefault()
    $(e.target).siblings().slideToggle('slow')
  })
});
