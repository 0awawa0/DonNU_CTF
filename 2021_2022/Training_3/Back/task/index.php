<?php

$username="Bobdl73";
$password="Tdmcd45PchJK";


echo '
      <html>
      <body>
	<h1>Authentication v0.01</h1>';

echo '
  <form action="" method="POST">
    Login&nbsp;<br/>
    <input type="text" name="username" /><br/><br/>
    Password&nbsp;<br/>
    <input type="password" name="password" /><br/><br/>
    <br/><br/>
    <input type="submit" value="submit" /><br/><br/>
  </form>
      </body>
      </html>';
if ($_POST["username"]!="" && $_POST["password"]!=""){
    if ($_POST["username"]==$username && $_POST["password"]==$password)
    {
      print("<h2>Welcome back {$row['username']} !</h2>");
      print("<h3>Information about you:</h3><p>- username : $row[username]</p><br />");
      print("To validate the challenge use this password. Flag input format: donnuCTF{password}</b>");
    } else {
      print("<h3>Error : Invalid user or password</h2><br />");

    }
}



?> 
