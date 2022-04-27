import RPi.GPIO as GPIO
import time

# Constant per controlar on volem la pilota amb un marge de 20 pixels
half = 320
full = 640
half_right = half + 20
half_left = half - 20
range_f = 300

def center_ball(x, pwm_1, pwm_2, m1, m2):
    if x == -1:
        pwm_1.ChangeDutyCycle(0)
        pwm_2.ChangeDutyCycle(0)
        return 0
    if x > half_left and x < half_right:
        print("On center")
        return 1
    elif x > half_right:
        GPIO.output(m1, True)
        GPIO.output(m2, False)
        speed = int((x/range_f - 1)*15 + 50)
        print("Turning right. Speed: ", speed)
        pwm_1.ChangeDutyCycle(int(30))
        pwm_2.ChangeDutyCycle(int(30))
        
    elif x < half_left:
        GPIO.output(m1, False)
        GPIO.output(m2, True)
        speed = int((1-x/range_f) * 15 + 50)
        print("Turning left. Speed: ", speed)
        pwm_1.ChangeDutyCycle(int(30))
        pwm_2.ChangeDutyCycle(int(30))
        
    return 0

def go_forward(pwm_1, pwm_2, m1, m2):
    GPIO.output(m1, True)
    GPIO.output(m2, True)
    pwm_1.ChangeDutyCycle(int(40))
    pwm_2.ChangeDutyCycle(int(40))
    print("Going forward")
    
e1 = 12
m1 = 10
e2 = 32
m2 = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(e1, GPIO.OUT)
GPIO.setup(m1, GPIO.OUT)
GPIO.setup(e2, GPIO.OUT)
GPIO.setup(m2, GPIO.OUT)


GPIO.output(m1, False)
GPIO.output(e1, True)
time.sleep(1)
GPIO.cleanup()





    
