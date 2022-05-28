import RPi.GPIO as GPIO
import time

# Function to go from angle to PWM signal
def AngleToDuty(ang):
  return float(ang)/10.+5.
  
#Setup servoPin as PWM output of frequancy 100Hz

def get_ball(pwm_w, pwm_a):
    # This function makes the arm get the ball once it is in position
    print("Getting ball")
    # First, we close the wrist
    pwm_w.ChangeDutyCycle(AngleToDuty(170))
    time.sleep(5)
    pwm_w.ChangeDutyCycle(AngleToDuty(140))
    time.sleep(0.2)
    pwm_w.ChangeDutyCycle(AngleToDuty(135))
    time.sleep(0.2)
    pwm_w.ChangeDutyCycle(AngleToDuty(130))
    time.sleep(0.2)
    pwm_w.ChangeDutyCycle(AngleToDuty(125))


    # Then, we elevate the arm to put the ball in the tube
    for i in range(170, 50, -2):
        pwm_a.ChangeDutyCycle(AngleToDuty(i))
        time.sleep(0.1)

    # We open the wrist
    pwm_w.ChangeDutyCycle(AngleToDuty(140))
    time.sleep(0.2)

    # We put down the arm
    for i in range(50, 176, 2):
        pwm_a.ChangeDutyCycle(AngleToDuty(i))
        time.sleep(0.1)

    # We open the wrist fully again to get the next ball
    pwm_w.ChangeDutyCycle(AngleToDuty(170))
    time.sleep(0.2)

    time.sleep(1)
    pwm_w.ChangeDutyCycle(0)
    pwm_a.ChangeDutyCycle(0)







