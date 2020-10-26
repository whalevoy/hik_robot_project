#!/usr/bin/env python

import rospy
import move_base
import actionlib
from std_msgs.msg import String 
from hik_robot_nav.msg import HikRobotSetTaskMsg
from geometry_msgs.msg import PoseStamped
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from smach_ros import SimpleActionState  


def callback(msg):
    group = msg.group

    position = msg.goal.target_pose.pose.position
    orientation = msg.goal.target_pose.pose.orientation

    print(rospy.get_caller_id(), 
            msg.group, 
            position.x, position.y, position.z,
            orientation.x, orientation.y, orientation.z, orientation.w)

    my_move_base = actionlib.SimpleActionClient("move_base", MoveBaseAction)
    msg.goal.target_pose.header.frame_id = 'map'
    msg.goal.target_pose.header.stamp = rospy.Time.now()
    
    my_move_base.send_goal(msg.goal)
    my_move_base.wait_for_result(rospy.Duration(10))
    print "successed!"
    #my_move_base.wait_for_result(rospy.Duration(10))
    #my_move_base.wait_for_result(rospy.Duration(10))
    #my_move_base.wait_for_result(rospy.Duration(10))


def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("HiRobotSetTaskMsg", HikRobotSetTaskMsg, callback)
    print('hik robot task topic is ready to get req.')
    rospy.spin()

if __name__ == '__main__':
    listener()
