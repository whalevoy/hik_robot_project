#!/usr/bin/env python

import rospy
import sys
from std_msgs.msg import String, Header
from move_base_msgs.msg import MoveBaseGoal
from geometry_msgs.msg import PoseStamped
from hik_robot_nav_test.msg import HikRobotSetTaskMsg

def talker():
    if  len(sys.argv) != 2 :
        print "need param set start/stop 1/0"
        return 0

    pub = rospy.Publisher('HiRobotSetTaskMsg', HikRobotSetTaskMsg, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(1)
    count = 0
    robot_goal = MoveBaseGoal()
    print sys.argv[1]
    if int(sys.argv[1]) == 0:
        print "stop"
        pub.publish(HikRobotSetTaskMsg(2,0,0,0,0,robot_goal))
    else:
        print "start" 
        pub.publish(HikRobotSetTaskMsg(2,0,1,0,0,robot_goal))


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
