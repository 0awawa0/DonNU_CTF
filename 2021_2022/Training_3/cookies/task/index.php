<?php
header('Content-Type: text/html; charset=utf-8');
error_reporting(0);

 $n = 0;
 if(!isset($_COOKIE["var"])) {
     setcookie ("var", $n);
	 
     echo "Welcome! Come here once more!";
 }
 else {
     $n = $_COOKIE["var"] + 1;
     setcookie ("var", $n);
	
     echo "You have visited this page ",$_COOKIE["var"], " times";
	 echo "<br>";
	 if($n==19){
		echo "Your flag is: donnuCTF{Y0u_sh0uld_be_0n_My_page_M0re}"; 
	 }
  }
  
  ?>
 <html>
 <body>
 <center>
 <div class="thumbnail">
<img src="cookie.jpg">
<div class="caption">
<h3>Tasty</h3>
</div>
</center>
 </body>
</html>