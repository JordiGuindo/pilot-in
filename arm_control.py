import RPi.GPIO as GPIO
import time

def AngleToDuty(ang):
  return float(ang)/10.+5.
  
#Setup servoPin as PWM output of frequancy 100Hz

def get_ball(pwm_w, pwm_a):
    print("Getting ball")
    pwm_w.ChangeDutyCycle(AngleToDuty(170))
    time.sleep(5)
    pwm_w.ChangeDutyCycle(AngleToDuty(140))
    time.sleep(0.2)
    pwm_w.ChangeDutyCycle(AngleToDuty(135))
    time.sleep(0.2)
    pwm_w.ChangeDutyCycle(AngleToDuty(130))
    time.sleep(0.2)
    pwm_w.ChangeDutyCycle(AngleToDuty(125))


    for i in range(170, 50, -2):
        pwm_a.ChangeDutyCycle(AngleToDuty(i))
        time.sleep(0.1)
        
    pwm_w.ChangeDutyCycle(AngleToDuty(130))
    time.sleep(0.2)

    for i in range(50, 176, 2):
        pwm_a.ChangeDutyCycle(AngleToDuty(i))
        time.sleep(0.1)
        
    pwm_w.ChangeDutyCycle(AngleToDuty(170))
    time.sleep(0.2)

    time.sleep(1)
    pwm_w.ChangeDutyCycle(0)
    pwm_a.ChangeDutyCycle(0)





