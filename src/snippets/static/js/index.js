$(document).ready(function() {
  $('#nav > div').hover(
	  function () {
	    var $this = $(this);
	    $this.find('.circle').stop().animate({
	      'width'     :'199px',
	      'height'    :'199px',
	      'top'       :'-25px',
	      'left'      :'-25px',
	      'opacity'   :'1.0'
	    },500,'easeOutBack',function(){
	      $(this).parent().find('ul').stop().fadeIn(700);
	    });
	
	    $this.find('a:first,h2,.fa').addClass('active');
	  },
	  function () {
	    var $this = $(this);
	    $this.find('ul').stop().fadeOut(500);
	    $this.find('.circle').stop().animate({
	      'width'     :'52px',
	      'height'    :'52px',
	      'top'       :'0px',
	      'left'      :'0px',
	      'opacity'   :'0.1'
	    },5000,'easeOutBack');
	
	    $this.find('a:first,h2,.fa').removeClass('active');
	  }
	);
	
	$('.try-button').on("click", function() {
		$input = $('.search-shnipit');
		$input.show();
		$input.animate({width: "300px"}, 300);
		$input.focus();
		$(this).removeClass("try-button").addClass("search-button");
		$(this).text("Search");
	});
});