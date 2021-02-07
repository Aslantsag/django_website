$(document).ready(function(){
	$('.header-nav__link').each(function(){
        if($(this).attr('href') == window.location.pathname){
			$(this).addClass('current');
		}
    });

    $('.send-post__btn').click(function(){
        $(this).toggleClass('open')
        $('.blog-sendpost-form').slideToggle();
    });

    $('#post-title').keyup(function(){
        $('#post-slug').val(generate_url($(this).val()));
    });

    if(window.location.pathname != '/'){
    	var text = $('.header-nav__link.current').text();
		$("#main").addClass('nothome');
		$(".nav_history span").text(text);
	}
	
});

window.onscroll = function() {
 	if(window.pageYOffset > 300){
 		document.querySelector('.header-scroll_down').classList.add('show');
 	}
 	else {
 		document.querySelector('.header-scroll_down').classList.remove('show');
 	}
 }

function generate_url(str){
    var url = str.replace(/[\s]+/gi, '-');
    url = translit(url);
    url = url.replace(/[^0-9a-z_\-]+/gi, '').toLowerCase();
    return url;
}

function translit(str){
    var ru=("А-а-Б-б-В-в-Ґ-ґ-Г-г-Д-д-Е-е-Ё-ё-Є-є-Ж-ж-З-з-И-и-І-і-Ї-ї-Й-й-К-к-Л-л-М-м-Н-н-О-о-П-п-Р-р-С-с-Т-т-У-у-Ф-ф-Х-х-Ц-ц-Ч-ч-Ш-ш-Щ-щ-Ъ-ъ-Ы-ы-Ь-ь-Э-э-Ю-ю-Я-я").split("-")
    var en=("A-a-B-b-V-v-G-g-G-g-D-d-E-e-E-e-E-e-ZH-zh-Z-z-I-i-I-i-I-i-J-j-K-k-L-l-M-m-N-n-O-o-P-p-R-r-S-s-T-t-U-u-F-f-H-h-TS-ts-CH-ch-SH-sh-SCH-sch-'-'-Y-y-'-'-E-e-YU-yu-YA-ya").split("-")
    var res = '';
    for(var i=0, l=str.length; i<l; i++){
        var s = str.charAt(i), n = ru.indexOf(s);
        if (n >= 0){
            res += en[n];
        }
        else {
            res += s;
        }
    }
    return res;
}

function scroll_to(pos = 0){
 	if(window.pageYOffset > 0){
 		document.querySelector('body, html').scrollTo({
 		    top: pos,
            behavior: 'smooth',
 		});
 	}
}