import RPi.GPIO as GPIO
import time

def AngleToDuty(ang):
  return float(ang)/10.+5.
  
#Setup servoPin as PWM output of frequancy 100Hz

wristPin=35
armPin =33
GPIO.setmode(GPIO.BOARD)
GPIO.setup(wristPin,GPIO.OUT)
GPIO.setup(armPin, GPIO.OUT)
pwm_w=GPIO.PWM(wristPin, 100)
pwm_a = GPIO.PWM(armPin, 100)

pwm_w.start(0) #star pwm
pwm_w.ChangeDutyCycle(AngleToDuty(170))
time.sleep(1)
pwm_w.ChangeDutyCycle(AngleToDuty(140))
time.sleep(0.2)
pwm_w.ChangeDutyCycle(AngleToDuty(135))
time.sleep(0.2)
pwm_w.ChangeDutyCycle(AngleToDuty(130))
time.sleep(0.2)
pwm_w.ChangeDutyCycle(AngleToDuty(125))


pwm_a.start(0) #star pwm
for i in range(170, 50, -5):
    pwm_a.ChangeDutyCycle(AngleToDuty(i))
    time.sleep(0.2)



time.sleep(1)
pwm_w.stop()
pwm_a.stop()
GPIO.cleanup()




