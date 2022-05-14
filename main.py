import cv2
import ball_detection as bd
import motor_control as mc
import numpy as np
import RPi.GPIO as GPIO
import time
import arm_control as ac


if __name__ == "__main__":
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
    
    wristPin=35
    armPin =33
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(wristPin,GPIO.OUT)
    GPIO.setup(armPin, GPIO.OUT)
    pwm_w=GPIO.PWM(wristPin, 100)
    pwm_a = GPIO.PWM(armPin, 100)


    # Inicializo PWM con un duty Cicle de cero
    pwm_1.start(0)
    pwm_2.start(0)
    vs = cv2.VideoCapture(0)
    pwm_w.start(0)
    pwm_a.start(0)
    
    counter_ball = 0
    

    
    
    while True:
        # Agafem el frame actual
        ret, frame = vs.read()
        if frame is None:
            break
        x, y, r = bd.detect_ball(frame)
        print(x, y)
        # Mostrem el frame per pantalla
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF
        
        
        c = mc.center_ball(x, pwm_1, pwm_2, m1, m2)
        
        if x > 240 and x < 360 and y > 390:
            counter_ball += 1
            pwm_1.ChangeDutyCycle(0)
            pwm_2.ChangeDutyCycle(0)
            print("Preparing to get_ball...")
        elif (c == 1):
            counter_ball = 0
            GPIO.output(m1, False)
            GPIO.output(m2, False)
            pwm_1.ChangeDutyCycle(35)
            pwm_2.ChangeDutyCycle(35)
            print("Going forward")
            
        if counter_ball == 20:
            ac.get_ball(pwm_w, pwm_a)
            print("Ball taken")
            
            
        if key == ord("q"):
            break
    
        
    pwm_1.stop()
    pwm_2.stop()
    pwm_w.stop()
    pwm_a.stop()
    GPIO.cleanup()
    vs.release()
    cv2.destroyAllWindows()
