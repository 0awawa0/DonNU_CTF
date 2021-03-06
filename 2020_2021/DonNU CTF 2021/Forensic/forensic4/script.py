from PIL import Image


def toBin(arr):
	res = ""
	for b in arr:
		res += f"{bin(b)[2:]:>08s}"
	return res


def lsb_hide(img, data):
	pixels = img.load()

	mask = ~0x01
	k = 0
	for i in range(img.height):
		for j in range(img.width):
			r, g, b = pixels[i, j]
			g = (g & mask) | (int(data[k % len(data)]) & 0x01)
			pixels[i, j] = (r, g, b)
			k += 1
	return pixels


archive = open("flag.zip", "rb").read()
image = Image.open("forensic4.png")
lsb_hide(image, toBin(archive))
image.save("forensic4_hid.png")
