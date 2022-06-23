var login;
var register;
var loginAcc;
var loginPW;
var regAcc;
var regPW;

function login(){
    loginAcc = document.getElementsByName("loginAcc")[0].value; //get登入帳號
    loginPW = document.getElementsByName("loginPW")[0].value;   //get登入密碼
    //console.log(loginAcc+" "+loginPW);
    var a = {"loginAcc":loginAcc,"loginPW":loginPW};
    var my = JSON.stringify(a);
    location.href = "login.php?package=" + my;    //丟登入帳號給php
    //丟登入密碼給php
}

function register(){
    regAcc = document.getElementsByName("regAcc")[0].value; //get註冊帳號
    regPW = document.getElementsByName("regPW")[0].value;   //get註冊密碼
    //console.log(regAcc+" "+regPW);
    var b = {"regAcc":regAcc,"regPW":regPW};
    var myb = JSON.stringify(b);
    location.href = "connect_test.php?package=" + myb; 
            //丟註冊帳號給php         //丟註冊密碼給php
}

function start(){
    login = document.getElementsByName("login")[0].addEventListener("click", login, false);     //
    register = document.getElementsByName("register")[0].addEventListener("click", register, false);        //
}

window.addEventListener("load", start, false);