import cv2
import ball_detection as bd
import motor_control as mc
import numpy as np
import RPi.GPIO as GPIO
import time
import arm_control as ac
import distance_sensor as ds


if __name__ == "__main__":
    # First, we initialize all of the pins
    
    # This pins control the wheel motors (e for speed, m for direction)
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
    
    # This two pins control the arm and the wrist
    wristPin=35
    armPin =33
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
    
    
    
    # This two pins control de distance sensor
    trigger = 13
    echo = 15
     
    #set GPIO direction (IN / OUT)
    GPIO.setup(trigger, GPIO.OUT)
    GPIO.setup(echo, GPIO.IN)
    
    # This timer is used for several things
    timer = time.time()
    
    # This variable is used to ensure the ball is in a correct position
    # for some iterations to pick it up
    counter_ball = 0
    

    while True:
        # We get the current frame
        ret, frame = vs.read()
        if frame is None:
            break
        x, y, r = bd.detect_ball(frame)
        print(x, y)
        # We show the frame with the ball detected (if there is one)
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF
        
        # This function tells the wheel motors how to move to center
        # the ball
        c = mc.center_ball(x, pwm_1, pwm_2, m1, m2)
        
        # If the ball is in a position where the arm can take it,
        # we wait for a few iterations until we are sure that is the case
        if x > 240 and x < 360 and y > 400:
            counter_ball += 1
            pwm_1.ChangeDutyCycle(0)
            pwm_2.ChangeDutyCycle(0)
            print("Preparing to get_ball...")
        elif (c == 1):
            counter_ball = 0
            mc.go_forward(pwm_1, pwm_2, m1, m2, y)
            
        # If the ball has been on a reachable position for 20 iterations,
        # we pick it up
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
