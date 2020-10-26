#!/usr/bin/env python

import rospy
from std_msgs.msg import String, Header
from move_base_msgs.msg import MoveBaseGoal
from geometry_msgs.msg import PoseStamped
from hik_robot_nav_test.msg import HikRobotSetTaskMsg

def talker():
    pub = rospy.Publisher('HiRobotSetTaskMsg', HikRobotSetTaskMsg, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(1)
    count = 0
    robot_goal = MoveBaseGoal()
    #robot_goal.target_pose = PoseStamped()
    #robot_goal.target_pose.header = Header()
    robot_goal.target_pose.header.frame_id = 'map'
    robot_goal.target_pose.pose.position.x = 0.112158038761
    robot_goal.target_pose.pose.position.y =  5.17669966938
    robot_goal.target_pose.pose.position.z = 4.69199491482e-08
    robot_goal.target_pose.pose.orientation.x = -1.5094644549e-08
    robot_goal.target_pose.pose.orientation.y = 1.16399754546e-07
    robot_goal.target_pose.pose.orientation.z = 0.734774907242
    robot_goal.target_pose.pose.orientation.w = 0.678311016929
    robot_goal.target_pose.header.stamp = rospy.Time(int(rospy.get_time()),34)
    #while not rospy.is_shutdown():
    hello_str = "req group %d" % count
    rospy.loginfo(hello_str)
    pub.publish(HikRobotSetTaskMsg(count,2,3,4,5,robot_goal))
    count = count + 1
    rate.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
