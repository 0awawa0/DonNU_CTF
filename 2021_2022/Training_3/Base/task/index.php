<?php 
error_reporting(-1);
ini_set('display_errors', 1);
//$page = (isset($_GET['page']) ? $_GET['page'] : "ctf1");
?>

<html>
<head>

</head>
<body>
<!--
Welcome on this portal!
I hope that you will enjoy your time among us, and above that all you will leave with lots of things in the head/
This is the second version of our portal. The project is at the alpha testing stage. 
In this regard, the appearance of the final product may differ significantly from the current one. 
Please report any errors that have occurred to mail@gmail.com

-->
<h1>Login v0.00002</h1>

<form action="index.php" method="POST">
    Password&nbsp;
    <input type="password" value="" name="passw"/><br/>
    <input type="submit" value="login"  name="submit" />
</form>
<?php

if (isset($_POST['submit'])){

	
	if ($_POST['passw']=="grm7DGy8VQazo57!FdjOP"){
		
		echo "<h3>ba5e_wi11_n0t_pr0vide_re1iable_pr0tection</h3>";
	}
	else {
		echo "<h3>Wrong password</h3>";

	}


}

?>
<!--
Richard, finally complete the login form. And do not forget to delete the comment with the password from the admin panel !!!



password=NHFXSFc4enh4aTV0eVQxRHZNV2U5V1dGV3B1RE1wZlp0N3ltMzlXbVFHYUtBZjdhREZMNTNicg==

</body>
</html>
