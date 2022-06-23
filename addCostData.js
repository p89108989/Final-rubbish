var button;//第一層按鈕
var submit;//第二層按鈕
var cardNum;
var price;
var dateTime;

function throwDB3(){
    var tempJSON = {"cardNum":cardNum, "price":price, "dateTime":dateTime};
    var myJSON = JSON.stringify(tempJSON);
    location.href = "addCostData.php?package=" + myJSON;
}

function myFunction3() {
    cardNum = document.getElementById("handmadecard").value;
    price = document.getElementById("handmadeprice").value;
    let date = document.getElementById("handmadeDate").value;
    let time = document.getElementById("handmadeTime").value;
    
    //時間字串處理
    let temp = date.split("-");
    date = temp[0] + temp[1] + temp[2];
    temp = time.split(":");
    time = temp[0] + temp[1];
    dateTime = date + time + '00';
    //字串轉數字
    cardNum = parseInt(cardNum);
    price = parseInt(price);
    dateTime = parseInt(dateTime);

    throwDB3();
}

function listen3(){
    submit = document.getElementsByName("addDataButton")[0];
    //submit = document.getElementById("updateButton");
    submit.addEventListener("click", myFunction3, false);
}

function start(){
    button = document.getElementById("thirdPic").addEventListener("click", listen3, false);
}

window.addEventListener("load", start, false);
