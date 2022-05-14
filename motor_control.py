import RPi.GPIO as GPIO
import time

# Constant per controlar on volem la pilota amb un marge de 20 pixels
half = 320
full = 640
half_right = half + 20
half_left = half - 40
range_f = 300
ratio = 0.87272

def center_ball(x, pwm_1, pwm_2, m1, m2):
    if x == -1:
        GPIO.output(m1, True)
        GPIO.output(m2, False)
        print("Ball not detected. Looking for ball.")
        pwm_1.ChangeDutyCycle(int(60))
        pwm_2.ChangeDutyCycle(int(60))
    if x > half_left and x < half_right:
        print("On center")
        return 1
    elif x > half_right:
        GPIO.output(m1, False)
        GPIO.output(m2, True)
        speed = int((x/range_f - 1)*15 + 50)
        print("Turning right")
        pwm_1.ChangeDutyCycle(int(40))
        pwm_2.ChangeDutyCycle(int(40))
        
    elif x < half_left:
        GPIO.output(m1, True)
        GPIO.output(m2, False)
        print("Turning left")
        pwm_1.ChangeDutyCycle(int(40))
        pwm_2.ChangeDutyCycle(int(40))
        
    return 0

def go_forward(pwm_1, pwm_2, m1, m2):
    GPIO.output(m1, True)
    GPIO.output(m2, True)
    pwm_1.ChangeDutyCycle(int(40))
    pwm_2.ChangeDutyCycle(int(40))
    print("Going forward")
   
"""
e1 = 12
m1 = 10
e2 = 32
m2 = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(e1, GPIO.OUT)
GPIO.setup(m1, GPIO.OUT)
GPIO.setup(e2, GPIO.OUT)
GPIO.setup(m2, GPIO.OUT)

pwm_1 = GPIO.PWM(e1, 500)
pwm_2 = GPIO.PWM(e2, 500)


# Inicializo PWM con un duty Cicle de cero
pwm_1.start(0)
pwm_2.start(0)

GPIO.output(m1, False)
GPIO.output(m2, False)
pwm_1.ChangeDutyCycle(48)
pwm_2.ChangeDutyCycle(48)
print("Going forward")
time.sleep(2)
pwm_1.stop()
pwm_2.stop()
GPIO.cleanup()"""

