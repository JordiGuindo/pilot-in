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
    
    
    # This variable is used to ensure the ball is in a correct position
    # for some iterations to pick it up
    counter_ball = 0
    
    # These variables are used to make the robot search for balls in different locations
    # If searching is False, the robot will be rotating. If it is True, it will be going forward.
    # We will also use it to make use of the distance sensor when going forward,
    # to avoid crashing
    searching = False
    # Counter_distance will be used for counting iterations. If the distance is close during
    # several iterations, the robot will stop and will rotate
    counter_distance = 0
    # Timer will help with changing the variable searching. If the robot does not find a ball
    # it will be rotating for 20 s and going forward for 3 s in a loop, unless the distance
    # sensor says otherwise
    t = 20
    t0 = time.time()
    

    while True:
        # We get the current frame
        ret, frame = vs.read()
        if frame is None:
            break
        x, y, r = bd.detect_ball(frame)
        # We show the frame with the ball detected (if there is one)
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF
        if x != -1:
            t0 = time.time()
        
        # This part of the code controls when the robot has to change between
        # rotating and going forward if the ball is not found
        t1 = time.time() - t0
        if t1 > t and x == -1:
            if not searching:
                # If the robot has to go forward, we ensure that there is not an obstacle in front
                # of it at least in a distance of 1 m
                pwm_1.ChangeDutyCycle(0)
                pwm_2.ChangeDutyCycle(0)
                time.sleep(0.2)
                d1 = ds.distance(trigger, echo)
                time.sleep(0.1)
                d2 = ds.distance(trigger, echo)
                time.sleep(0.1)
                if d1 > 60 and d2 > 60:
                    print("There is not an in front object. Going forward")
                    t = 15
                    searching = True
                    t0 = time.time()
                else:
                    # If there is an obstacle, we keep rotating for 5 more seconds
                    print("There is an obstacle. Keep rotating")
                    t0 = time.time() - 15
            else:
                print("Let's look for a ball in this position")
                t = 20
                searching = False
                t0 = time.time()
            
        # This function tells the wheel motors how to move with the purpose of centering the ball
        # so the robot can take it. It also tells them how to move if there is not a ball
        c = mc.center_ball(x, pwm_1, pwm_2, m1, m2, searching)
        
        if searching and x == -1:
            d = ds.distance(trigger, echo)
            time.sleep(0.07)
            if d < 70:
                counter_distance += 1
            if counter_distance > 5:
                print("Object too close. Start rotating")
                t = 20
                searching = False
                t0 = time.time()
                counter_distance = 0
                
        
        
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
