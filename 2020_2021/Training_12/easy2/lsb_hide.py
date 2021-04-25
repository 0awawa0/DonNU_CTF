from PIL import Image


def bytes_to_bin(data):
	return "".join(f"{bin(i)[2:]:>08}" for i in data)

def hide_lsb_image(image, binary):
	pixels = image.load()
	for i in range(image.height):
		for j in range(image.width):
			r, g, b = pixels[j, i]
			bit = int(binary[i % len(binary)])
			r = (r & (~0x01)) | bit
			g = (g & (~0x01)) | bit
			b = (b & (~0x01)) | bit
			pixels[j, i] = (r, g, b)
	return pixels


data = b"donnuCTF{d52127b1b3f17805675280653e10fb66}"
image = Image.open("easy2.png")
hide_lsb_image(image, bytes_to_bin(data))
image.save("encoded.png")