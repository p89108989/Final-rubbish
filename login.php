<?php
$result;
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
    $acc =  $account_id["loginAcc"];
    $bcc =  $account_id["loginPW"];
    $sql = "SELECT * FROM login_system WHERE account_id ='" .$acc. "'";
    echo $sql;
    $result = mysqli_query($link, $sql) or die("錯誤訊息：".mysqli_error($link));
    $row = mysqli_fetch_assoc($result);
    if($row["account_password"]==$bcc)
    {   
        setcookie( "test", "$acc", time()+3600);
        echo ("<script>window.location.href='TheBestWeCanDo.html'</script>"); 
    }
    else
    {
        echo "<script>window.alert('login failed --有一個錯 自己想');</script>";
        echo ("<script>window.location.href='JokeOnYou.html'</script>"); 
    }
    
}
else {
    echo "不正確連接資料庫</br>" . mysqli_connect_error();
}
?>