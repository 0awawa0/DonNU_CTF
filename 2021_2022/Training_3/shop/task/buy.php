<?php
if (isset($_POST)) {
//print_r($_POST);
$id=$_POST['id'];
$price = (int)$_POST['price'];
if ($id=='0' && $price < 100) {
include("buysuccess.html");
}
else if($id=='1')
{include("buytrash.html");}
else {include("buy.html");}
}
?>
