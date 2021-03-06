from PIL import Image


def unhide_bits(image):
	image_pixels = image.load()
	counter = 0
	result = ""
	for x in range(image.height):
		for y in range(image.width):
			r, g, b = image_pixels[y, x]
			mask = 0b00000001
			if counter == 0:
				result += str(r & mask)
			elif counter == 1:
				result += str(g & mask)
			else:
				result += str(b & mask)
			counter = (counter + 1) % 3
	return result


image1 = Image.open("encoded.png")
res = int(unhide_bits(image1), 2)
print(res.to_bytes((res.bit_length() + 7) // 8, "big")[:40])
image1.close()