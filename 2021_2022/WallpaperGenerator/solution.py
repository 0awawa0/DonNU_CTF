import time
import random
from PIL import Image


img = Image.open('get_image.png')
pixels = img.load()


timestamp = round(time.time())
while True:
	centers = []
	random.seed(timestamp)
	for _ in range(42):
		x = random.randint(50, img.width - 50)
		y = random.randint(50, img.height - 50)
		while (x, y) in centers:
			x = random.randint(50, img.width - 50)
			y = random.randint(50, img.height - 50)
		centers.append((x, y))

	flag = ""
	for i in range(42):
		p = pixels[centers[i][0], centers[i][1]]
		flag += chr(p[1])
	
	if flag[:5] == "donnu":
		print(flag)
		break

	timestamp -= 1