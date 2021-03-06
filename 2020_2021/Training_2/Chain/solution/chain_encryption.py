

def encrypt(text, iv):
	result = b""
	current_key = iv
	for char in text:
		result += bytes([(char + current_key) % 256])
		current_key = (char + current_key) % 256
	return result


def decrypt(text, iv):
	result = b""
	last_key = iv
	current_key = iv
	for char in text:
		t = (char - current_key) % 256
		result += bytes([t])
		current_key = (current_key + t) % 256
	return result

if __name__ == "__main__":
	iv = int(input("Enter initial chain value >> ")) % 256
	encrypted = open("encrypted.txt", 'rb').read()
	decrypted = decrypt(encrypted, iv)
	print(decrypted)