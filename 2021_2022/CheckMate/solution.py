from PIL import Image
from textwrap import wrap


def binToText(binary): return b"".join(bytes([int(i, 2)]) for i in wrap(binary, 8))


def decodeFlag(img):

	pixels = img.load()
	currentPosition = (0, 0)
	vertical = False
	channel = 0
	bits = ""
	mask = 1

	while (currentPosition[0] < img.width and currentPosition[1] < img.height):

		r, g, b = pixels[currentPosition]

		if (channel == 0): bits += str(r & mask)
		elif (channel == 1): bits += str(g & mask)
		else: bits += str(b & mask)

		if (vertical):
			currentPosition = (currentPosition[0] + 1, currentPosition[1] + 2)
		else:
			currentPosition = (currentPosition[0] + 2, currentPosition[1] + 1)

		vertical = not vertical
		channel = (channel + 1) % 3

	return binToText(bits)


if __name__ == "__main__":

	img = Image.open("encoded.png")
	print(decodeFlag(img))