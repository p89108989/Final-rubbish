var name;
var phonenumber;
var creditcard;
var email;
var submit;
var button;


function link(){
    name = document.getElementsByName("link_name")[0].value;
    phonenumber = document.getElementsByName("link_name")[0].value;
    creditcard = document.getElementsByName("link_name")[0].value;
    email = document.getElementsByName("link_name")[0].value;

    var linklist ={"name":name, "phonenumber":phonenumber, "creditcard":creditcard, "email":email};
    var toDB = JSON.stringify(linklist);
    location.href = "linking.php?package=" + toDB;
}

function listen(){
    submit = document.getElementsByName("link_submit")[0];
    submit.addEventListener("click", link, false);
}

function start(){
    button = document.getElementById("linking").addEventListener("click", listen, false);
}

window.addEventListener("load", start, false);