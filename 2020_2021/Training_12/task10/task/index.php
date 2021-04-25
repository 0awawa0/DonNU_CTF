<html>
    <head>
        <title>SOURCE</title>
        <style>
            #main {
    height: 100vh;
}
        </style>
    </head>
    <body><center>
	</br>
	</br>
	</br>
	</br>
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
 <form action="index.php" method="post">
    <input type="text" name="number"><br><br>
    <button name="submit">Отправить</button><br><br>
	<p><a href="source.txt" hidden="hidden">Source is helpful</a></p>
<?php

if(isset($_POST["submit"])) {
  $web = $_POST["number"];

  if (is_numeric($web)){
    if (strlen($web) < 5){
		  if ( $web > 10000){
        echo ('<div class="w3-panel w3-green"><h3>Correct</h3><p>donnuCTF{strl3n_1s_1ntr1cat3}</p></div>');
		  } else {
        echo ('<div class="w3-panel w3-red"><h3>Wrong!</h3><p>Ohhhhh!!! Closer  </p></div>');	
		  }
	  } else {
        echo ('<div class="w3-panel w3-red"><h3>Wrong!</h3><p>Nice!!! Near But Far</p></div>');
    }
  } else {
    echo ('<div class="w3-panel w3-red"><h3>Wrong!</h3><p>Ahhhhh!!! It is not a number!</p></div>');
  }
}
?>
</center>
<!-- Source is helpful -->
    </body>
</html>