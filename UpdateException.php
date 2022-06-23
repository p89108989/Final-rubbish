<?php
    $loginAcc;
    $result;
    $price;
    $times;
    $timeStart;
    $timeEnd;
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
        $price = $JSON["price"];
        $times = $JSON["times"];
        $loginAcc = $_COOKIE["test"];
        $timeStart = $JSON["startTime"];
        $timeEnd = $JSON["endTime"];
        $sql = "SELECT * FROM time_limit WHERE account_id ='$loginAcc'";
        $result = mysqli_query($link, $sql) or die("錯誤訊息：".mysqli_error($link));
        $row = mysqli_fetch_assoc($result);
        echo $row["account_id"];
        if($row["account_id"])
        {
        echo $row["account_id"];
        $sql = "update time_limit set time_start='$timeStart"."00"."', time_finish='$timeEnd"."00"."' where account_id = '$loginAcc'";
        }
        else
        {
        $sql = "INSERT INTO time_limit (account_id,time_start,time_finish) VALUES ('$loginAcc','$timeStart','$timeEnd') ";
        }
        mysqli_query($link, $sql)or die("錯誤訊息：".mysqli_error($link));
        $sql = "update login_system set predict_money_custom='$price', cost_in_one_hour='$times' where account_id = '$loginAcc'";
        mysqli_query($link, $sql)or die("錯誤訊息：".mysqli_error($link));
        echo ("<script>window.location.href='TheBestWeCanDo.html'</script>");
    }
    else {
        echo "不正確連接資料庫</br>" . mysqli_connect_error();
    }
?>