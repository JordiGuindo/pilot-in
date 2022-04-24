import cv2
import imutils
import random

# Per ara, aquest codi només detecta pilotes taronges a través d'imatge

vs = cv2.VideoCapture(0)

# Definim thresholds per detectar el color taronja
orangeLower = (0, 52, 112)
orangeUpper = (9, 202, 255)


while True:
	# Agafem el frame actual
	ret, frame = vs.read()
	if frame is None:
		break
	# Després de fer Gaussiana, passem a espai HSV
	frame = imutils.resize(frame, width=600)
	blurred = cv2.GaussianBlur(frame, (11, 11), 0)
	hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

	# Fem la máscara pel color taronja
	mask = cv2.inRange(hsv, orangeLower, orangeUpper)
	mask = cv2.erode(mask, None, iterations=2)
	mask = cv2.dilate(mask, None, iterations=2)
	cv2.imshow("Mask", mask)

	# Trobem els contorns
	cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	center = None

	if len(cnts) > 0:
		# Trobem el contorn més gran (el de la pilota més propera) i l'utilitzem per obtenir
		# les coordenades del centre de la pilota en pantalla i el radi
		c = max(cnts, key=cv2.contourArea)
		((x, y), radius) = cv2.minEnclosingCircle(c)
		M = cv2.moments(c)
		center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
		# El cercle ha de tenir una mida mínima
		if radius > 10:
			# Amb aquest codi, dibuixem el cercle
			cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
			cv2.circle(frame, center, 5, (0, 0, 255), -1)
			if random.randint(1, 10) == 10:
				print("(", x, ", ", y, ")", radius)
	# Mostrem el frame per pantalla
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF

	if key == ord("q"):
		break

vs.release()
cv2.destroyAllWindows()

