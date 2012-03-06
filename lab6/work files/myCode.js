$(document).ready(function(){
	//	alert('ready!');
	$('#task1 .button').click(function() {
		$('#task1 #firstheading').css('color', 'red');
	});
	$('#task2 .button').click(function() {
		$('#task2 .secondheading').text('I have been changed');
	});
	//alert('ready!');
	$('#task3 .button').click(function() {
		//alert('.button');	
		$('#task3 .pony').attr('src', 'http://4.bp.blogspot.com/-uzYNCnWSaKU/TefdmBsNo8I/AAAAAAAAAWM/bRghjGUNHwo/s1600/515924929_0d814d9f0c.jpg');
	});
	
	$('#task4 .button').click(function() {
		$('#task4 #prison #bars').remove();
	});
	$('#money .button').click(function() {
		$('#money img').each(function() {
			var h = $(this).height() + 20;
			var w = $(this).width() + 20;
			//alert(h + " " + w);
			$(this).css({width:w, height:h});
		});
	});

	$('#car .button').click(function() {
		$('#car img').animate({left:'+=250'});
	});

	$('#nyan .nyancat').click(function() {
		$(this).animate({left: '+=250'});
			
		$('#nyan .rainbows').css({width: $('#nyan .rainbows').width()+250+'px'});
	});
});
