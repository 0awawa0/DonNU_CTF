<?php
  $servername = 'database';
  $username  = 'level2';
  $password = 'level2';
  $database = 'level2';
  $flag = "donnuCTF{4b6d575adb84981d27e5794a149d9a4d}";

  // Create connection
  $conn = new mysqli($servername, $username, $password, $database);

  // Check connection
  if ($conn->connect_error) {
      die("Unable to connect to MYSQL server");
  }
?>
