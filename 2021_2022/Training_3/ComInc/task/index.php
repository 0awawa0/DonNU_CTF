<html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
</head>
<body>
<h1>Grep</h1>
<div id="content">
<form>
Find words containing: <input name=needle><input type=submit name=submit value=Search><br><br>
</form>
Output:
<?php
$key = "";

if(array_key_exists("needle", $_REQUEST)) {
    $key = $_REQUEST["needle"];
}

if($key != "") {
    system("grep $key fileflag.txt");
    #system("findstr $key fileflag.txt");
}
?>
<div id="viewsource"><a href="index-source.txt">View sourcecode</a></div>
</div>
</body>
</html>