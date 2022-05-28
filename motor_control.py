import RPi.GPIO as GPIO
import time

# Constants to control the position where we want the ball to be in the image to pick it up
half = 320
full = 640
half_right = half + 20
half_left = half - 40
range_f = 300

def center_ball(x, pwm_1, pwm_2, m1, m2, searching):
    # This function tells the motors how to move taking into account the x position of the ball
    # in the image

    # If there is no ball and we are not going forward, the motors rotate the robot
    if x == -1 and not searching:
        GPIO.output(m1, True)
        GPIO.output(m2, False)
        print("Ball not detected. Looking for ball. Rotating")
        pwm_1.ChangeDutyCycle(int(65))
        pwm_2.ChangeDutyCycle(int(65))
        return -1
    # If there is no ball and we are going forward, the motors move the robot forward
    if x == -1 and searching:
        GPIO.output(m1, False)
        GPIO.output(m2, False)
        print("Ball not detected. Looking for ball. Going forward")
        pwm_1.ChangeDutyCycle(int(47))
        pwm_2.ChangeDutyCycle(int(47))
        return -1
    # If there is a ball, and it is already centered in the image, we will go forward
    if x > half_left and x < half_right:
        print("On center")
        return 1
    # If there is a ball on the right of the screen, the robot turns right
    elif x > half_right:
        GPIO.output(m1, False)
        GPIO.output(m2, True)
        speed = int((x/range_f - 1)*15 + 50)
        print("Turning right")
        pwm_1.ChangeDutyCycle(int(55))
        pwm_2.ChangeDutyCycle(int(55))
    # If there is a ball on the left of the screen, the robot turns left
    elif x < half_left:
        GPIO.output(m1, True)
        GPIO.output(m2, False)
        print("Turning left")
        pwm_1.ChangeDutyCycle(int(60))
        pwm_2.ChangeDutyCycle(int(60))
        
    return 0

def go_forward(pwm_1, pwm_2, m1, m2, y):
    # This function makes the robot go forward when the ball is already centered. 
    GPIO.output(m1, False)
    GPIO.output(m2, False)
    if y > 300:
        speed = 45
    else:
        speed = 50
    pwm_1.ChangeDutyCycle(speed)
    pwm_2.ChangeDutyCycle(speed)
    print("Going forward")


