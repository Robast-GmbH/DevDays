usefull comands:

//verkehr auf topic sehen:
ros2 topic echo <topic>   

//auf topic publishen
ros2 topic pub <topic> <msg type> <data>

ros2 topic list
ros2 topic info


ros2 interface show
ros2 interface list

// zeigt alle laufenden services an
ros2 service list

// call service
ros2 service call <service> <data type> <data>

ros2 pkg create --build-type ament_python <name> --dependencies rclpy example_interfaces 
colcon build --symlink-install


nettes tool:
rqt