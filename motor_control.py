import RPi.GPIO as GPIO
import time

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

# Definimos que los motores vayan hacia delante
GPIO.output(m1, True)
GPIO.output(m2, False)

# Inicializo PWM con un duty Cicle de cero
pwm_1.start(0)
pwm_2.start(0)




try:
    pwm_1.ChangeDutyCycle(int(60))
    pwm_2.ChangeDutyCycle(int(60))
    time.sleep(5) 
except:
    pwm_1.stop()
    pwm_2.stop()
    GPIO.cleanup()
    
pwm_1.stop()
pwm_2.stop()
GPIO.cleanup()


    
