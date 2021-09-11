import cv2


reader = cv2.VideoCapture("result.mp4")

res, img = reader.read()
counter = 0
imgCount = 0

while res:
	counter += 1
	if counter % 73 == 0:
		cv2.imwrite(f"decoded_{imgCount}.jpg", img)
		imgCount += 1
	res, img = reader.read()

reader.release()
