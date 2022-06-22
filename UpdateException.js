var button
var submit
let price
let times
let startTime
let endTime

function myFunction() {
  //document.getElementById("price").innerHTML = "Hello World";
  console.log("111");
  let price = document.getElementById("price").value;
  let times = document.getElementById("times").value;
  let startTime = document.getElementById("TimeStart").value;
  let endTime = document.getElementById("TimeEnd").value;
  console.log(price+" \n"+times+" \n"+startTime+" \n"+endTime);
  console.log("222");
}

function test1(){
    console.log("456");
}
function test2(){
    console.log("789");
}

/*function start(){
    console.log("123");
    //document.getElementById("submitButton").addEventListener("click", test1, false);
    //document.getElementsByName("updateButton").click = test();
    //button = document.getElementsByName("updateButton").addEventListener("click", test2, false);
    //document.getElementsByName("updateButton").addEventListener("click", test2, false);
    //console.log("123");
    //let button = document.getElementById("submitButton").addEventListener("onclick", myFunction, false);
}*/
function listen(){
    console.log("789");
    /*setTimeout(function(){
        console.log("I am the third log after 5 seconds");
        
    },5000);*/
    submit = document.getElementsByName("updateButton");
    //submit = document.getElementById("updateButton");
    submit.addEventListener("click", myFunction, false);
    console.log("987");
}

function start(){
    console.log("456");
    button = document.getElementById("secPic").addEventListener("click", listen, false);
    console.log("654");
}

window.addEventListener("load", start, false);
//loadDOMContentLoaded