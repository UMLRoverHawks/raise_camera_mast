#!/usr/bin/env python
import rospy
from std_msgs.msg import Bool
from lib_robotis import *

def callback(data):
	if data.data == True:
            dyn = USB2Dynamixel_Device('/dev/camera_mast_servo')
            p = Robotis_Servo( dyn, 2 )
            p.move_angle( math.radians( -11 ), blocking = False )
	    if p.is_moving() == True:
                while True:
	             if p.is_moving() == False:
		         p.disable_torque()
		         rospy.signal_shutdown('Done')

def raise_camera_mast():
    rospy.init_node('raise_camera_mast', anonymous=False)
    rospy.Subscriber('raise_camera_mast', Bool, callback)
    rospy.spin()


if __name__ == '__main__':
    raise_camera_mast()
