function sayHello() {
   alert("Hello World")
}


function verifyPassword(){
	alert()
	alert($("#pwd").val())
	if($("#pwd").val()!=$("#cnf_pwd").val())
	{
		alert("Password and confirm password does not match!");
		return false;
	}	
}