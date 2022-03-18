usefull comands:

verkehr auf topic sehen:
ros2 topic echo <topic>   

auf topic publishen
ros2 topic pub <topic> <msg type> <data>

ros2 topic list
ros2 topic info


ros2 interface show
ros2 interface list 

ros2 pkg create --build-type ament_python <pkg name> --dependencies rclpy <andere noch nötige z.B. std_msgs>
colcon build --symlink-install


nettes tool:
rqt