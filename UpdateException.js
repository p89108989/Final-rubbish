var button
var submit
let price
let times
let startTime
let endTime

function myFunction() {
    let price = document.getElementById("price").value;
    let times = document.getElementById("Times").value;
    let startTime = document.getElementsByName("timeStart")[0].value;
    let endTime = document.getElementsByName("timeEnd")[0].value;
    console.log(price+" \n"+times+" \n"+startTime+" \n"+endTime);
}

function listen(){
    submit = document.getElementsByName("updateButton")[0];
    //submit = document.getElementById("updateButton");
    submit.addEventListener("click", myFunction, false);
}

function start(){
    button = document.getElementById("secPic").addEventListener("click", listen, false);
}

window.addEventListener("load", start, false);
