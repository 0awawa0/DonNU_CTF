<?php
header('Content-Type: text/html; charset=utf-8');
error_reporting(0);
$n1=hash('sha256', 'flag'); 
$str='cookieMonster'; 
$n = hash('sha256', $str); 
setcookie ("name", $n1); 
$n2=$_COOKIE["name"];
if($n2=='fa824713120008e66941339e4c824f2bc09434492d91a1cb680fb02561539563'){
	echo "Your flag is: donnuCTF{M0nster_d0esnt_bite_Me}"; 
	 }
  
  ?>
 <!DOCTYPE html>

<html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>cookieMonster</title>
    <link rel="stylesheet" href="./cookieMonster_files/style.css">
  </head>
  <body>
    <h1>cookieMonster</h1>
<p>Welcome to cookieMonster challenge!</p>
<img src="./cookieMonster_files/cookieMonster.jpg" style="display: block">

  <!-- 73656e64206d6520736861323536206f66206d79206e616d65 -->

</body></html>