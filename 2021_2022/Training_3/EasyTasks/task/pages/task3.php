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
<body style="color: #000000">
	<div class="content tc">
		<div class="title">Задание #3</div>
		<form>
			Попытайтесь снова
		</form>
	</div>
	<script>
		const rgb2hex = (rgb) => `#${rgb.match(/^rgb\((\d+),\s*(\d+),\s*(\d+)\)$/).slice(1).map(n => parseInt(n, 10).toString(16).padStart(2, '0')).join('')}`

		function check() {
			let pw = rgb2hex(document.body.style.color);
			let pass = prompt("Для получения доступа введите пароль","");
			if (pass == pw) {
				function _0x1a69(){var _0xfee43b=['2364lRdykZ','2sXCUEF','is\x20Qr9L_h8','1886759xdHBgu','6OpcTZr','90185PHsZEk','44mPKHOD','Your\x20flag\x20','48578DfYSUN','6030ohWprn','1287309TJAhIz','11693bxkexz','2219832DngEXb','1640CqRTjg','bA_RMhB_Wd'];_0x1a69=function(){return _0xfee43b;};return _0x1a69();}function _0x546d(_0x11c07a,_0x4cda6b){var _0xd9789a=_0x1a69();return _0x546d=function(_0x1c0f3b,_0x32dd11){_0x1c0f3b=_0x1c0f3b-(-0x5d1+0x152d*-0x1+0x1*0x1bbd);var _0x4bbc1b=_0xd9789a[_0x1c0f3b];return _0x4bbc1b;},_0x546d(_0x11c07a,_0x4cda6b);}var _0x503081=_0x546d;(function(_0x59f398,_0x1fe4ce){var _0x28a759=_0x546d,_0x38bae6=_0x59f398();while(!![]){try{var _0x37c6f7=parseInt(_0x28a759(0xc0))/(0x3*-0x33f+0x10e3+-0x725)+-parseInt(_0x28a759(0xc8))/(-0x1a1d*0x1+0x2a*0x16+-0x33*-0x71)*(-parseInt(_0x28a759(0xc2))/(0x194f+0x1789*-0x1+-0x1c3))+parseInt(_0x28a759(0xcd))/(0x2*-0x100a+0x1e64+0x1b4)*(parseInt(_0x28a759(0xcc))/(0xbf*0x1+0xb*-0x91+-0x581*-0x1))+-parseInt(_0x28a759(0xcb))/(0x2*-0x6d3+0xabe+0x2ee)*(parseInt(_0x28a759(0xca))/(-0x4a*-0x42+-0x1492+0x185))+parseInt(_0x28a759(0xc4))/(0x20bd+-0x8*0x493+0x3e3*0x1)+parseInt(_0x28a759(0xc1))/(-0x1*-0x10bf+0x7a3*0x3+-0x279f)*(-parseInt(_0x28a759(0xc5))/(-0xe44+-0x1cc8+0x2b16))+-parseInt(_0x28a759(0xc3))/(-0x22af*0x1+0xb1*0x29+0x17*0x47)*(parseInt(_0x28a759(0xc7))/(-0x246+0xae5+-0x5*0x1b7));if(_0x37c6f7===_0x1fe4ce)break;else _0x38bae6['push'](_0x38bae6['shift']());}catch(_0x2d77c5){_0x38bae6['push'](_0x38bae6['shift']());}}}(_0x1a69,-0x24a30+-0x2ca94+-0x5*-0x2211b),alert(_0x503081(0xbf)+_0x503081(0xc9)+_0x503081(0xc6)+'ha'));
				window.location.href = "/pages/task4/";
			}
		}

		check();
	</script>
</body>
</html>