<?php
$name = $_GET['fuck'];
$account_id=$_GET['value'];
$account_password=$_GET['value'];
$host = '203.204.10.191';
$dbuser ='admin';
$dbpassword = 'PASSWORD';
$dbname = 'test';
$link = mysqli_connect($host,$dbuser,$dbpassword,$dbname);
if($link){
    mysqli_query($link,'SET NAMES uff8');
    echo "正確連接資料庫";
    $sql = "INSERT INTO login_system (account_id) VALUES ('$name') ";
    mysqli_query($link, $sql) or die("錯誤訊息：".mysqli_error($link));
}
else {
    echo "不正確連接資料庫</br>" . mysqli_connect_error();
}
?>