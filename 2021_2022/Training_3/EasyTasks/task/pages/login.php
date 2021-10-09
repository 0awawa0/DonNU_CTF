<?
	$loggedIn = FALSE;
	$flag = "Ваш флаг: <i class=\"green\">xygL_raCm_h7rt_cXut</i>"; // Подставить название переменной вместо логина
	$secret = "";
	$l = $_POST['login'];

	if (!isset($_COOKIE["admin"])) {
		setcookie("admin", "false");
	} else {
		if ($_COOKIE["admin"] === "true") {
			$secret = "YzGX_XCt4_Wj8e_T5uV"; // 2
			$loggedIn = true;
			setcookie("admin", "false");
		}
	}

	if (!$loggedIn && isset($_POST["login"]) && isset($_POST["password"])) {
		if (is_numeric($_POST["password"])) {
			$_POST["password"] = (int)$_POST["password"];
		}
		if ($_POST["login"] === "Admin" && $_POST["password"] == "********") {
			if ($_POST["password"] === "********") {
				$secret = "pyhM_vj2G_QYyX_S5Uh"; // 1
				$loggedIn = true;
			} else {
				$secret = "EysQ_vMxf_ZV3Q_avp5"; // 3
				$loggedIn = true;
			}
		}
	}
	if (strlen($secret) > 0) {
		$secret = "Ваш флаг: <i class=\"green\">$secret</i>";
	}
?>
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8"/>
		<meta http-equiv="Pragma" content="no-cache"/>
		<link rel="stylesheet" href="/pageStyle.css">
		<link rel="stylesheet" href="/indexStyle.css">
		<style>
			.content {
				padding: 2rem;
				padding-top: 1rem;
			}
		</style>
</head>
<body>
	<div class="content tc">
	<? if (isset($_POST["login"]) && isset($_POST["password"])) { ?>
		<div class="title">Аккаунт <i class="green"><? eval("echo \"$l\";"); ?></i></div>
			<? if(!$loggedIn) { ?>
				<span><i class="red">Ошибка! </i> Неверный логин или пароль.</span>
			<? } else { ?>
				<span><i class="green">Успех! </i> Вы вошли в аккаунт администратора.</span>
			<? }
			echo "<span>$secret</span>";
			?>
			<input type="button" class="middle" onclick="window.location.href = window.location.href;" value="Вернуться" />
		<? } else { ?>
		<div class="title">Панель авторизации</div>
		<form method="POST" action="">
			<input type="text" name="login" />
			<input type="text" name="password" value="******" minlength="8" maxlength="8" />
			<input type="submit" name="submit" />
		</form>
	<? } ?>
	</div>
</body>
</html>