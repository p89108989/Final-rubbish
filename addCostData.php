<?php
    $loginAcc;
    $result;
    $cardNum;
    $price;
    $dateTime;
    $name = $_GET['package'];
    $JSON=json_decode($name,true);
    $host = '203.204.10.191';
    $dbuser ='admin';
    $dbpassword = 'PASSWORD';
    $dbname = 'test';
    $link = mysqli_connect($host,$dbuser,$dbpassword,$dbname);
    if($link){
        mysqli_query($link,'SET NAMES utf8');
        echo "正確連接資料庫";
        $cardNum = $JSON["cardNum"];
        $price = $JSON["price"];
        $loginAcc = $_COOKIE["test"];
        $dateTime = $JSON["dateTime"];
        $sql = "INSERT INTO predict_module(creditNum,money,cost_time,account_id) VALUES ('$cardNum','$price','$dateTime','$loginAcc') ";
        $result = mysqli_query($link, $sql) or die("錯誤訊息：".mysqli_error($link));
        echo ("<script>window.location.href='TheBestWeCanDo.html'</script>");
    }
    else {
        echo "不正確連接資料庫</br>" . mysqli_connect_error();
    }
?>