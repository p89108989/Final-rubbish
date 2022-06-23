<?php
    $loginAcc;
    $result;
    $name;
    $phonenumber;
    $creditcard;
    $email;
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
        $name = $JSON["name"];
        $phonenumber = $JSON["phonenumber"];
        $loginAcc = $_COOKIE["test"];
        $creditcard = $JSON["creditcard"];
        $email = $JSON["email"];
        $sql = "INSERT INTO login_system(num_ber,credit_card_number,email) VALUES ('$phonenumber','$creditcard','$email','$loginAcc') ";
        $sql = "update login_system set num_ber='$phonenumber', credit_card_number='$creditcard',email='$email' where account_id = '$loginAcc'";
        $result = mysqli_query($link, $sql) or die("錯誤訊息：".mysqli_error($link));
        $row = mysqli_fetch_assoc($result);
        echo ("<script>window.location.href='TheBestWeCanDo.html'</script>");
    }
    else {
        echo "不正確連接資料庫</br>" . mysqli_connect_error();
    }
?>