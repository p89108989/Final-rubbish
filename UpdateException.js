var button;
var submit;
var price;
var times;
var startTime;
var endTime;

function throwDB(){
    var tempJSON = {"price":price, "times":times, "startTime":startTime, "endTime":endTime};
    var myJSON = JSON.stringify(tempJSON);
    location.href = "UpdateException.php?package=" + myJSON;
}

function myFunction() {
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

    throwDB();
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
