

def encrypt(text, iv):
	result = b""
	current_key = iv
	for char in text:
		result += bytes([(char + current_key) % 256])
		current_key = (char + current_key) % 256
	return result


def decrypt(text, iv):
	result = b""
	return result


if __name__ == "__main__":
	iv = int(input("Enter initial chain value >> ")) % 256
	text = open("text.txt", 'rb').read()
	encrypted = encrypt(text, iv)
	print(encrypted)
	decrypted = decrypt(encrypted, iv)
	print(decrypted)
	open("encrypted.txt", 'wb').write(encrypted)