from base64 import b64decode

# Читаем байты картинки
data = open("1.jpg", "rb").read()

for i in range(10):

	# Проверяем сигнатуру файла
	first_bytes = data[:2]

	# По сигнатуре определяем JPG или PNG. Ищем индекс сигнатуры конца картинки
	if first_bytes == b"\x89\x50":
		index = data.find(b"\x49\x45\x4e\x44\xae\x42\x60\x82")
		bias = 8  # Так как индекс указывает на начало сигнатуры, то надо добавить смещение на длину сигнатуры
		print("Image is PNG")
	else:
		index = data.find(b"\xff\xd9")
		bias = 2
		print("Image is JPEG")

	# Читаем данные для декодирования
	data_to_decrypt = data[index + bias:]

	# Ищем индекс первого разделителя и считываем алгоритм кодировки
	separator1 = data_to_decrypt.find(b":")
	algorithm = data_to_decrypt[:separator1]

	# Срезаем данные об алгоритме вместе с разделителем
	data_to_decrypt = data_to_decrypt[separator1 + 1:]

	if algorithm == b"base64":
		print("\tAlgorithm is base64\n")

		# Для Base64 больше ничего делать не надо, можно сразу декодировать данные и переходить к следующей итерации
		data = b64decode(data_to_decrypt)

	elif algorithm == b"hex":
		print("\tAlgorithm is hex\n")

		# Для hex сначала переводим данные в число
		data = int(data_to_decrypt[2:].decode(), 16)

		# Переводим числов байты и переходим к следующей итерации
		data = data.to_bytes((data.bit_length() + 7) // 8, "big")

	elif algorithm == b"xor":

		# Для xor ищем индекс следующего разделителя и считваем ключ
		separator2 = data_to_decrypt.find(b":")
		key = int(data_to_decrypt[:separator2].decode())

		print("\tAlgorithm is xor")
		print("\t\tKey is " + str(key) + "\n")

		# Расшифровываем остальные данные с помощью полученного ключа и переходим к следующей итерации
		data = bytes([i ^ key for i in data_to_decrypt[separator2 + 1:]])

	elif algorithm == b"rot":

		# Так же для ROT, сначала получаем ключ, потом расшифровываем
		separator2 = data_to_decrypt.find(b":")
		key = int(data_to_decrypt[:separator2].decode())

		print("\tAlgorithm is rot")
		print("\t\tKey is " + str(key) + "\n")

		data = bytes([(i - key) % 256 for i in data_to_decrypt[separator2 + 1:]])

	else:
		print("Something went wrong")
		open("dump.dmp", "wb").write(data)
		exit()

# После 10 итераций выводим данные
print(data)
