<?php
  include 'secret.php';
  if($_GET["str1"] and $_GET["str2"]) {
    if ($_GET["str1"] !== $_GET["str2"] and
        hash("md5", $salt . $_GET["str1"]) === hash("md5", $salt . $_GET["str2"])) {
      echo $flag;
    } else {
      echo "Nope.";
    }
    exit();
  }
?>
<!DOCTYPE html>
<html>
<body>
  <h2>MD5 Collission</h2>
  <p>
    Well this one is easy. Just send me two distinct strings with equal MD5 hashes and you will get your flag
  </p>
  <p>
    Also, here's the <a href="src.php">source code</a>.
  </p>
  <form method="GET">
    String 1: <input type="text" name="str1">
    <br>
    String 2: <input type="text" name="str2" style="margin-top: 10px;">
    <br>
    <input type="submit" style="margin-top: 10px;">
  </form>
</body>
</html>