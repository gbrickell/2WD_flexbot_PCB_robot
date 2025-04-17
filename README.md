# 2WD flexbot PCB robot
Raspberry Pi Zero managed 2WD robot using the flexbot v7.0 PCB

&nbsp; &nbsp; <img src="images\2WD_robot.jpg" width="360" height="333">

An early (late 2019) compact/3-plate robot design using 3D printed components and the flexbot v7.0 PCB - much more project detail is available from [here](https://onlinedevices.org.uk/RPi_flexbot_PCB_2WD_robot) and the 3D printed component designs can be downloaded from [here](https://www.printables.com/model/1267019-raspberry-pi-2wd-flexbot-robot).

The design for the PCB, shown in the 3 images below, can be downloaded from the PCB_design_files folder as gerber files.

<img src="images\flexbot_PCB07_front01_400w.jpg" width="235" height="420"> &nbsp; &nbsp; <img src="images\flexbot_PCB07_back02_400w.jpg" width="234" height="420">  &nbsp; &nbsp; <img src="images\flexbot_PCB07_back01_400w.jpg" width="258" height="420">

The software for this robot uses a mixture of Python and compiled 'C' code with the flexbot01_gpio.c code compiled to create a .so library that can be used by the Python code using the ctypes library. It should also be noted that this development was carried out on a relatively old/low powered Raspberry Pi Zero that was still using the Buster OS and no validation/updates have carried out for the newest/latest Raspberry Pi OS version.

 Some of the initial component testing code can be downloaded from the software folder, but the main operational code is still being finalised and will be added here in due course.
