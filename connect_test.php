<?php
$acc;
$bcc;
$name = $_GET['package'];
$account_id=json_decode($name,true);
$account_password=$_GET['value'];
$host = '203.204.10.191';
$dbuser ='admin';
$dbpassword = 'PASSWORD';
$dbname = 'test';
$link = mysqli_connect($host,$dbuser,$dbpassword,$dbname);
if($link){
    mysqli_query($link,'SET NAMES uff8');
    echo "正確連接資料庫";
    $acc =  $account_id["regAcc"];
    $bcc =  $account_id["regPW"];
    $sql = "INSERT INTO login_system (account_id,account_password) VALUES ('$acc','$bcc') ";
    echo $sql;
    mysqli_query($link, $sql) or die("錯誤訊息：".mysqli_error($link));
    echo ("<script>window.location.href='TheBestWeCanDo.html'</script>");
}
else {
    echo "不正確連接資料庫</br>" . mysqli_connect_error();
}
?>