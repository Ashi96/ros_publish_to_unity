# ros_publish_to_unity
publish to unity with ros
## Requirement
- Computer
  - AlienWare R13
- Operation System
  - Ubuntu 16.04
- ROS
  - ROS kinetic kame
## How to use
##### Install
~~~
$ cd ~/catkin_ws/src
$ git clone https://github.com/Ashi96/ros_publish_to_unity.git
$ cd ../ && catkin_make
~~~
##### Publish
~~~
$ roscore
~~~
Another terminal
~~~
$ rosrun ros_publish_to_unity chat.py
ex) display "Hello World!!"
Hello World!!
~~~
## License
- MIT License  
This software is released under the MIT License, see LICENSE.txt
