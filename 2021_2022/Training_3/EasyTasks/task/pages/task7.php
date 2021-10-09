<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8"/>
	<meta http-equiv="Pragma" content="no-cache"/>
	<link rel="stylesheet" href="/pageStyle.css">
	<style>
		.content {
			padding: 2rem;
			padding-top: 1rem;
		}
	</style>
</head>
<body bg="/files/fff.png">
	<div class="content tc">
		<div class="title">Задание #7</div>
		<form method="POST" action="/pages/task_checker" >
			Введите пароль
			<input type="password" name="password"/>
			<input type="submit" name="submit" value="Войти" />
			<input type="hidden" name="task" value="7" />
		</form>
	</div>
</body>
</html>