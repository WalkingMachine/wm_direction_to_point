# wm_direction_to_point

## Overview
service that gives an angle between two points.

    **Author(s): Huynh-Anh Le 
            (Annie-Anh)


#### Building

	cd catkin_ws/src
	git clone https://github.com/WalkingMachine/wm_direction_to_point.git
	cd ../
	catkin_make

## Usage
Run the main node with

    roscore
    roslauch <your_robot>_description <your_robot>_description.launch
	rosrun wm_direction_to_point frames.py
	
#### Services

    name: get_direction
    descriptionL: get two points and calculate the angle
    between them.

#### ADVICES

    Open rviz for better visualition :)
