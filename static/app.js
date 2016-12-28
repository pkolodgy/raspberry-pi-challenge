$(document).ready(function() {

  $('header').on('submit', '#fruit-search', function(e){
    e.preventDefault();
    var fruit = $("input[name='fruit_name']").val()
    $.ajax({
      method: $(e.target).attr('method'),
      url: '/'+fruit+'/pie'
    })
    .done(function(r) {
      var results = r['results']
      results.forEach(function(recipe) {
        $('body').append(recipe['title'])
      })
    })
  })
});
