function send_yanzheng()
{
	var email = $("#nameinput").val();
	$.post("/yanzheng", {"email": email}, function(data){
			alert(data)}
	);
}
