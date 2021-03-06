import pyminizip
import os
import random
from PIL import Image
from string import ascii_lowercase, digits


alphabet = ascii_lowercase + digits

braile_alphabet = {
	'a': [[1, 0], [0, 0], [0, 0]],
	'b': [[1, 0], [1, 0], [0, 0]],
	'c': [[1, 1], [0, 0], [0, 0]],
	'd': [[1, 1], [0, 1], [0, 0]],
	'e': [[1, 0], [0, 1], [0, 0]],
	'f': [[1, 1], [1, 0], [0, 0]],
	'g': [[1, 1], [1, 1], [0, 0]],
	'h': [[1, 0], [1, 1], [0, 0]],
	'i': [[0, 1], [1, 0], [0, 0]],
	'j': [[0, 1], [1, 1], [0, 0]],
	'k': [[1, 0], [0, 0], [1, 0]],
	'l': [[1, 0], [1, 0], [1, 0]],
	'm': [[1, 1], [0, 0], [1, 0]],
	'n': [[1, 1], [0, 1], [1, 0]],
	'o': [[1, 0], [0, 1], [1, 0]],
	'p': [[1, 1], [1, 0], [1, 0]],
	'q': [[1, 1], [1, 1], [1, 0]],
	'r': [[1, 0], [1, 1], [1, 0]],
	's': [[0, 1], [1, 0], [1, 0]],
	't': [[0, 1], [1, 1], [1, 0]],
	'u': [[1, 0], [0, 0], [1, 1]],
	'v': [[1, 0], [1, 0], [1, 1]],
	'w': [[0, 1], [1, 1], [0, 1]],
	'x': [[1, 1], [0, 0], [1, 1]],
	'y': [[1, 1], [0, 1], [1, 1]],
	'z': [[1, 0], [0, 1], [1, 1]],
	'#': [[0, 1], [0, 1], [1, 1]],
	'1': [[1, 0], [0, 0], [0, 0]],
	'2': [[1, 0], [1, 0], [0, 0]],
	'3': [[1, 1], [0, 0], [0, 0]],
	'4': [[1, 1], [0, 1], [0, 0]],
	'5': [[1, 0], [0, 1], [0, 0]],
	'6': [[1, 1], [1, 0], [0, 0]],
	'7': [[1, 1], [1, 1], [0, 0]],
	'8': [[1, 0], [1, 1], [0, 0]],
	'9': [[0, 1], [1, 0], [0, 0]],
	'0': [[0, 1], [1, 1], [0, 0]]
}


def drawLetter(letter, backgroundColor, letterColor, padRight = 2, padLeft = 2):

	letterWidth = 3

	width = letterWidth + padLeft + padRight
	img = Image.new("RGB", (width, 9), backgroundColor)

	braile = braile_alphabet[letter]

	if braile[0][0]:
		img.putpixel((padLeft + 0, 2), letterColor)

	if braile[0][1]:
		img.putpixel((padLeft + 2, 2), letterColor)

	if braile[1][0]:
		img.putpixel((padLeft + 0, 4), letterColor)

	if braile[1][1]:
		img.putpixel((padLeft + 2, 4), letterColor)

	if braile[2][0]:
		img.putpixel((padLeft + 0, 6), letterColor)

	if braile[2][1]:
		img.putpixel((padLeft + 2, 6), letterColor)

	if letter.isdigit():
		prefix = drawLetter('#', backgroundColor, letterColor, padRight, padLeft)
		return joinImages(prefix, img)
	else:
		return img


def joinImages(img1, img2):
	img = Image.new("RGB", (img1.width + img2.width, min(img1.height, img2.height)))
	img.paste(img1, (0, 0))
	img.paste(img2, (img1.width, 0))
	return img


def stringToBraileImage(string, backgroundColor = None, letterColor = None):
	if backgroundColor == None:
		backgroundColor = random.randint(0, 2 ** 24 - 1)

	if letterColor == None:
		letterColor = random.randint(0, 2 ** 24 - 1)
		while letterColor == backgroundColor:
			letterColor = random.randint(0, 2 ** 24 - 1)

	if len(string) == 0: 
		return None

	if len(string) == 1:
		return drawLetter(string, backgroundColor, letterColor)

	result = drawLetter(string[0], backgroundColor, letterColor, padRight = 2)

	for i in range(1, len(string) - 1):
		result = joinImages(result, drawLetter(string[i], backgroundColor, letterColor, padLeft = 2, padRight = 2))

	return joinImages(result, drawLetter(string[-1], backgroundColor, letterColor, padLeft = 2))


# file = "flag.txt"

password = "".join([random.choice(alphabet) for i in range(8)])
stringToBraileImage(password).save("pwd0.png")
print(f"Flag password: {password}")

pyminizip.compress("flag.txt", "", "flag.zip", password, 9)
zipFile = "flag.zip"

for i in range(100):
	password = "".join([random.choice(alphabet) for i in range(8)])
	print(f"Password {i + 1}: {password}")

	pyminizip.compress_multiple([zipFile, f"pwd{i}.png"], ["", ""], f"{i + 1}.zip", password, 9)
	stringToBraileImage(password).save(f"pwd{i + 1}.png")

	os.remove(f"pwd{i}.png")
	os.remove(zipFile)
	zipFile = f"{i + 1}.zip"

pyminizip.compress_multiple([f"{i + 1}.zip", f"pwd{i + 1}.png"], ["", ""], f"{i + 2}.zip", "", 9)
os.remove(zipFile)