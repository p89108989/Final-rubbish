var name1;
var phonenumber;
var creditcard;
var email;
var submit;
var button;


function link(){
    console.log("789")
    name1 = document.getElementsByName("link_name")[0].value;
    phonenumber = document.getElementsByName("link_PhoneNum")[0].value;
    creditcard = document.getElementsByName("link_creditcard")[0].value;
    email = document.getElementsByName("link_email")[0].value;

    //console.log(name1+" "+phonenumber+" "+creditcard+" "+email);

    var linklist ={"name":name1, "phonenumber":phonenumber, "creditcard":creditcard, "email":email};
    var toDB = JSON.stringify(linklist);
    location.href = "linking.php?package=" + toDB;
}

function start(){
    submit = document.getElementsByName("link_submit")[0];
    submit.addEventListener("click", link, false);
}

window.addEventListener("load", start, false);