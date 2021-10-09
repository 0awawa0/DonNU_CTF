<?php 
error_reporting(-1);
ini_set('display_errors', 1);
//$page = (isset($_GET['page']) ? $_GET['page'] : "ctf1");
?>

<html>
<head>

</head>
<body>

<?php

if ($_SERVER['HTTP_USER_AGENT']=="True admin"){
	echo "<h4>Welcome young padawan! Flag:Us3r_Ag3n7_1s_easy_70_replace</h4>";
}
else {
	echo "<h4>Wrong user-agent. This not the 'True admin' browser!</h4>";
}
?>


</body>
</html>
