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
	<div class="content index">
		<div class="title">Задания</div>
		<div class="cards-container">
			<div class="card tc" id="card1">Level 1</div>
			<div class="card tc" id="card2">Level 2</div>
		</div>
	</div>
	<div class="card-content">
		<div class="close" onclick="unloadPage()"></div>
		<div class="title">Описание</div>
		<div class="desc"></div>
	</div>
	<script>
		let cards = document.getElementsByClassName("card");
		for (let i = 1; i <= cards.length; i++) {
			cards[i-1].onclick = () => { loadPage(i); };
		}

		function loadPage(id) {
			document.getElementsByClassName("card-content")[0].classList.add("active");
			let desc = document.getElementsByClassName("desc")[0];
			switch(id) {
				case 1:
					desc.innerHTML = "Прежде чем перейти на 2 уровень сложности, докажите свою решимость. Найдите <a href=\"/pages/task1\" target=\"_blank\" class=\"blue\">здесь</a> все флаги!";
					break;
				case 2:
					desc.innerHTML = "Вам дана <a href=\"/pages/login\" target=\"_blank\" class=\"blue\">панель авторизации</a>. Попробуйте войти от имени администратора различными способами. Здесь можно найти <i class=\"green\">5</i> флагов, логин: <i class=\"green\">Admin</i>. Желаем удачи.";
					break;
			}
			setTimeout(() => {
				document.getElementsByClassName("card-content")[0].classList.add("loaded");
			}, 350);

		}

		function unloadPage() {
			document.getElementsByClassName("card-content")[0].classList.remove("loaded");
			setTimeout(() => {
				document.getElementsByClassName("card-content")[0].classList.remove("active");
			}, 350);
		}
	</script>
</body>
</html>