<img src="https://github.com/JordiGuindo/pilot-in/blob/main/images/PILOT-IN.jpeg" align="right" width="300" alt="header pic"/>

# PILOT-IN
This robot recognises ping-pong balls using computer vision and gets them with the help of an arm. It stores them in a removable case. 

# Table of Contents
   * [What is this?](#what-is-this)
   * [Requirements](#requirements)
   * [Amazing contributions](#amazing-contributions)
   * [Hardware](#hardware)
   * [Software](#software)
   	 * [Image capture](#image-capture)
   	 * [Distance sensor module](#distance-sensor-module)
   	 * [Ball detecion](#ball-detection)
	 * [Motion planner](#motion-planner)
   	 * [Wheel control](#wheel-control)
	 * [Arm control](#arm-control)
   * [Contribution](#contribution)
   * [Citing](#citing)
   * [Authors](#authors)
   * [Bibliography](#biblio)
# What is this?
This is our final project for the Robotics, Language and Planification (RLP) subject at the Universitat Autonoma de Barcelona (UAB). 
We presented PILOT-IN, a robot whose objective is to recognise ping-pong balls and pick them up. Here bellow, we explain how the robot was built and how we made it work correctly.
# Requirements
- Coding Requirements
	- [Python 3.10.x](https://www.python.org/)
	- [NumPy](https://numpy.org/)
	- [OpenCV](https://opencv.org/)
- Electronic components
	- Raspberry Pi 3B
	- Raspberry Pi Camera V2
	- Motor Dual controller H-Bridge v1.3
	- Standard servomotor 3001 HB (2)
	- HC-SR04 ultrasonic distance sensor
	- Wheels (2) and crazy wheel
	- Pololu micrometal motors 75:1 (2)
- 3D pieces
	- They are all [here](https://github.com/JordiGuindo/pilot-in/tree/main/3D)
# Amazing contributions
Our robot is aimed at professional ping pong athletes. It will be used in the specific situation where the athlete needs to train a certain aspect of the game for which it is necessary to use several balls. Our robot allows the athlete to train without the help of anyone to collect the balls, which improves the efficiency of training and contributes to the improvement of results in the competition.  
The robot is able to make individual workouts much more efficient, without the need to have people picking up balls.
It can also be used if you are not a professional athlete, but the full potential of the robot will not be exploited, as it will not be used as often. However, it can help to prevent back pain, as it will not be necessary to bend down to look for all the balls. It can be used in cases of therapy, if there has been an injury to the arm. If rehabilitation involves throwing a ball, it may be helpful to the patient.  
On the other hand, our robot is scalable. The design can be adapted for different sports, and different capacities (maximum number of balls collected). Depending on the sport played, the different components of the robot can be changed to collect the balls based on what the playing field is like, what the size of the balls is and what the optimal number of balls to be loaded is.  

# Hardware
The following picture shows how all the electronic components are connected. 
<img src="https://github.com/JordiGuindo/pilot-in/blob/main/images/hardware.jpg"/>  
The Raspberry PI is the brain of PILOT-IN.  
All motors are connected to pins that can give PWM signals, so we can control the amount of power
they recieve. In the case of the wheel motors, we have two cables coming out of the RPi to control each one of them. One controls the speed, the other the direction. 
This connects to the Motor Dual Controller, which will give the corresponding power to the motors. 
With the servomotors only one cable is necessary. Motors are powered by external batteries, 7.2 V for the wheel ones and 6 V for the servomotors.\n
We took advantage of the power supply the RPi can give to power the HC-SR04 ultrasonic sensor. However, a voltage divisor has to be used for the echo pin, 
since the RPi cannot take an input of more than 3.3 V.  
Lastly, we have camera connected to it.    
On the other hand, we used 3D printing to ensemble the full robot. Here is how the final ensemble of this pieces looks like (the black pieces represent the electronic components):
<img src="https://github.com/JordiGuindo/pilot-in/blob/main/images/final_ensemble.png"/>  

# Software
In the following picture are depicted the different software modules. The inputs and outputs of each module can be seen.  
<img src="https://github.com/JordiGuindo/pilot-in/blob/main/images/software_modules.jpg"/>
### Image capture
This module takes care of capturing the image that the camera sees. It is implemented directly with the functions that OpenCV provides.
### Distance Sensor Module  
The only library needed for this module is the GPIO library, that allows to control the pins of the RPi. It is entirely in the distance_sensor.py file.
### Ball detection
For this module, the OpenCV library is needed. To detect the balls we use two filters for the image that comes from the Image Capture module: a color filter
and a shape filter. These can be changed. After applying the color filter, a binary image is obtain, where the white pixels represent the color we are looking for.
After that, the shape filter is used to discard other possible objects with the same color. Lastly, we use some OpenCV functions to draw a circle around the ball:  
<img src="https://github.com/JordiGuindo/pilot-in/blob/main/images/ball_detection.jpg"/>  
This module is coded in the ball_detection.py file. 
### Motion planner
This is the main module. Depending on what this module recieves from the previous ones, it tells the motors to behave in different ways in order to approach the ball
and get it. It has two modes: the searching mode and the target mode. 
- Searching mode: if a ball is not detected in the ball detection module, the robot will try to find one in the room. This mode uses the ultrasonic distance sensor
to avoid big obstacles, like walls or table legs. PILOT-IN will alternate between moving forward and turning around itself while looking for the ball.
- Target mode: when a ball is detected in the ball detection module, the robot will approach it until it is placed in a reachable position for the arm. Depending on the 
position of the ball, the robot will go forward or will turn left or right. When the ball is in a reachable position, a function is called so the arm moves to pick it up. 
In the following gif, you can see the what the robot sees and how it approaches the ball:
<img src="https://github.com/JordiGuindo/pilot-in/blob/main/images/motion_planner.gif"/>  
This module is coded in the main.py file.  
### Wheel control 
This module focuses on doing the control part of the wheels by by using Raspberry PI's signals. Therefore, we use this signals to operate and control the DC motors calling some functions that manage these signals. 
The GPIO library is used for that. All of it is coded in the motor_control.py file.  
### Arm control 
This module has the same function as the Wheel Control module, but this module focuses on the arm control. It uses functions and the signals of the Raspberry PI to control the movement of the arm, needed to move the balls into the tube/box.
The GPIO library is also used here. It is coded in the arm_control.py file. 

# Contribution
Feel free to contribute with anything that could potentially improve the project, whether it be design, software architecture, code, hardware components.... Anything is welcomed, and we appreciate contributions.
If you feel like it, feel free to contact the owner of this GitHub. 

# Citing
If you use this project of academic work or industry, please cite it. 
Use this format:   
"PILOT-IN, a robot that uses computer vision to detect and pickup sport balls", 2022, name of the authors (our names), link to this GitHub.

# Authors
Sergi Sánchez Hernández  
Francisco A. Molina Bakhos  
Jordi Guindo Martínez  
Ferran Anton Serrano  

# Bibliography
This project has been inspired by the following Internet projects:
"Robot recogepelotas", MECATRONICA ESPE LATACUNA ECUADOR - SUDAMÉRICA, https://www.youtube.com/watch?v=108TMEKc74c  
“Sistema autónomo para recolección de bolas de tenis mediante vision artificial”, D. Gaitán Tabares, H. Martínez Arcila. Universidad Distrital Francisco José Caldas, 2015.  
Here you can find what we have used to code the robot: 
"Teach, Learn, and Make with Raspberry PI", https://www.raspberrypi.org/  
"RPi.GPIO - PyPI", https://pypi.org/project/RPi.GPIO/
"OpenCV", https://opencv.org/

