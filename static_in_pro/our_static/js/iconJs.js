$(document).ready(function(){
		$("#genderLayer").hide();
		$("#attLayer").hide();
		
		$("#countryLayer input").click(function(){
			if (this.checked==true){
				$(this).parent().addClass("orange");				
				$(this).parent().parent().parent().slideUp(1000);
				$(this).parent().parent().parent().next().slideDown(1000);
				if($(this).parent().siblings().hasClass("orange")){
					$(this).parent().siblings().removeClass("orange");
				};
			};
		});
		$("#genderLayer input").click(function(){
			if (this.checked==true){
				$(this).parent().addClass("orange");				
				$(this).parent().parent().parent().slideUp(1000);
				$(this).parent().parent().parent().next().slideDown(1000);
				if($(this).parent().siblings().hasClass("orange")){
					$(this).parent().siblings().removeClass("orange");
				};
			};
		});
		$("#attLayer input").click(function(){

			if (this.checked==true){
				$(this).parent().addClass("orange");
				if($(this).parent().siblings().hasClass("orange")){
					$(this).parent().siblings().removeClass("orange");
				};
			};
			
		});
		$(".icon.icon-xiangshang.return-icon").click(function(){
			$(this).parent().hide();
			$(this).parent().prev().show();
		});

	});