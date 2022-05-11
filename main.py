import cv2
import ball_detection as bd
import motor_control as mc
import numpy as np
import RPi.GPIO as GPIO
import time


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


    # Inicializo PWM con un duty Cicle de cero
    pwm_1.start(0)
    pwm_2.start(0)
    vs = cv2.VideoCapture(0)

    while True:
        # Agafem el frame actual
        ret, frame = vs.read()
        if frame is None:
            break
        x, y, r = bd.detect_ball(frame)
        # Mostrem el frame per pantalla
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF

        c = mc.center_ball(x, pwm_1, pwm_2, m1, m2)
        
        if (c == 1):
            GPIO.output(m1, False)
            GPIO.output(m2, False)
            pwm_1.ChangeDutyCycle(40)
            pwm_2.ChangeDutyCycle(int(40*0.87272))
            print("Going forward")
            
        if key == ord("q"):
            break

        
    pwm_1.stop()
    pwm_2.stop()
    GPIO.cleanup()
    vs.release()
    cv2.destroyAllWindows()
