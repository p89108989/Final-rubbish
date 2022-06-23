var button;
var submit;
var price;
var times;
var startTime;
var endTime;
var loginAcc;
var loginButton;

function throwDB2(){
    //location.href = ".php?price=" + price;
    //location.href = ".php?times=" + times;
    //location.href = ".php?startTime=" + startTime;
    //location.href = ".php?endTime=" + endTime;

    var tempJSON = {"loginAcc":loginAcc, "price":price, "times":times, "startTime":startTime, "endTime":endTime};
    var myJSON = JSON.stringify(tempJSON);
    location.href = "UpdateException.php?package=" + myJSON;
}

function myFunction2() {
    price = document.getElementById("price").value;
    times = document.getElementById("Times").value;
    startTime = document.getElementsByName("timeStart")[0].value;
    endTime = document.getElementsByName("timeEnd")[0].value;

    //時間字串處理
    let temp = startTime.split(":");
    startTime = temp[0] + temp[1];
    temp = endTime.split(":");
    endTime = temp[0] + temp[1];

    //字串轉數字
    price = parseInt(price);
    times = parseInt(times);
    startTime = parseInt(startTime);
    endTime = parseInt(endTime);

    throwDB2();
}


function listen2(){
    submit = document.getElementsByName("updateButton")[0];
    //submit = document.getElementById("updateButton");
    submit.addEventListener("click", myFunction2, false);
}

function start(){
    button = document.getElementById("secPic").addEventListener("click", listen2, false);
}

window.addEventListener("load", start, false);
