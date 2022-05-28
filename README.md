<img src="https://github.com/JordiGuindo/pilot-in/blob/main/images/PILOT-IN.jpeg" align="right" width="300" alt="header pic"/>

# PILOT-IN
This robot recognises ping-pong balls using computer vision and gets them with the help of an arm. It stores them in a removable case. 

# Table of Contents
   * [What is this?](#what-is-this)
   * [Requirements](#requirements)
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
and get it. 

