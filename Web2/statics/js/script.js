$(document).ready(function(){
	$("#login").click(function(){
		var user = $("#username").val();
		var pwd = $("#password").val();
		var pd ={"username":user,"password":pwd};
		$.ajax({
			type:"post",
			url:"/",
			data:pd,
			cache:false,
			success:function(){
				alert(data);
			},
			error:function(){
				alert("error!");
			},
		});
	});
});