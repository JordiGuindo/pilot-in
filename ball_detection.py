import cv2
import imutils

# We define boundaries for the mask to detect the balls by its color
orangeLower = (0, 118, 175)
orangeUpper = (180, 210, 255)

def detect_ball(frame):
    # After a GaussianBlurr, we transform to HSV space
    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    # We do the color mask
    mask = cv2.inRange(hsv, orangeLower, orangeUpper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=4)

    # We find the contours
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    center = None

    if len(cnts) > 0:
        # We find the biggest contour (the nearest ball) and get the position in the image
        # and the radius to get position and distance to the ball
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        # The circle has to have a minimum radius
        if radius > 10:
            # We draw the circle
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)
        return x, y, radius
    return -1, -1, -1

