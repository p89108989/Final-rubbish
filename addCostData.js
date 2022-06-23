var button;
var loginButton;

function start(){
    button = document.getElementById("thirdPic").addEventListener("click", listen, false);
    loginButton = document.getElementsByName("login")[0].addEventListener("click", login, false);
}

window.addEventListener("load", start, false);