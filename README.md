<img src="https://github.com/JordiGuindo/pilot-in/images/PILOT-IN.jpeg" align="right" width="300" alt="header pic"/>

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
	- They are all [here](https://github.com/JordiGuindo/pilot-in/3D/)
