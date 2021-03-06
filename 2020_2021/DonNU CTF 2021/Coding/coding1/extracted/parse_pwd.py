from PIL import Image


braile_letters = {
	32: 'a',
	48: 'b',
	36: 'c',
	38: 'd',
	34: 'e',
	52: 'f',
	54: 'g',
	50: 'h',
	20: 'i',
	22: 'j',
	40: 'k',
	56: 'l',
	44: 'm',
	46: 'n',
	42: 'o',
	60: 'p',
	62: 'q',
	58: 'r',
	28: 's',
	30: 't',
	41: 'u',
	57: 'v',
	23: 'w',
	45: 'x',
	47: 'y',
	43: 'z',
	15: '#'
}

braile_digits = {
	32: '1',
	48: '2',
	36: '3',
	38: '4',
	34: '5',
	52: '6',
	54: '7',
	50: '8',
	20: '9',
	22: '0'
}


def readChar(pixels, offset, backgroundColor):
	currPixel = offset
	startX = currPixel[0]

	char = []

	while currPixel[0] < startX + 3:
		char.append([])

		while currPixel[1] <  7:
			if pixels[currPixel[0], currPixel[1]] == backgroundColor:
				char[-1].append(0)
			else:
				char[-1].append(1)
			currPixel[1] += 2

		currPixel[0] += 2
		currPixel[1] = 2

	return char


def charMatrixToInt(matrix):
	res = ""
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			res += str(matrix[i][j])
	return int(res, 2)


def parsePwd(filename):

	img = Image.open(filename)
	pixels = img.load()
	backgroundColor = pixels[0, 0]
	offset = [2, 2]

	isNextDigit = False
	password = ""
	while offset[0] < img.width - 2:
		char = readChar(pixels, offset[:], backgroundColor)
		code = charMatrixToInt(char)

		try:
			if isNextDigit:
				password += braile_digits[code]
				isNextDigit = False
			else:
				if braile_letters[code] == '#':
					isNextDigit = True
				else:
					password += braile_letters[code]
		except Exception as ex:
			print(ex)
			print(char)

		offset[0] += 7

	return password


if __name__ == "__main__":
	filename = input("File to parse >> ")
	img = Image.open(filename)
	pixels = img.load()
	for i in range(img.width):
		for j in range(img.height):
			print(f"{i}:{j} - {pixels[i, j]}")
	print(parsePwd(filename))