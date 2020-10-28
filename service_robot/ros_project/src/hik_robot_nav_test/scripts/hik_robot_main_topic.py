#!/usr/bin/env python

import rospy
import move_base
import actionlib
from std_msgs.msg import String 
from hik_robot_nav_test.msg import HikRobotSetTaskMsg, HikRobotSetModules
from geometry_msgs.msg import PoseStamped
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from smach_ros import SimpleActionState  



def patrol_task(msg):
    print "patrol task running"
    my_move_base = actionlib.SimpleActionClient("move_base", MoveBaseAction)
    msg.goal.target_pose.header.frame_id = 'map'
    msg.goal.target_pose.header.stamp = rospy.Time.now()
    my_move_base.send_goal(msg.goal)
    my_move_base.wait_for_result(rospy.Duration(10))

def follow_task(msg):
    if msg.cmd == 0:
        print "follow task stop"
        pub = rospy.Publisher('HiRobotSetModules', HikRobotSetModules, queue_size=10)
        pub.publish(HikRobotSetModules(0,0,0))
    else:
        print "follow task start"
        pub = rospy.Publisher('HiRobotSetModules', HikRobotSetModules, queue_size=10)
        pub.publish(HikRobotSetModules(0,0,1))


def callback(msg):
    group = msg.group

    position = msg.goal.target_pose.pose.position
    orientation = msg.goal.target_pose.pose.orientation

    print(rospy.get_caller_id(), 
        msg.group, 
        position.x, position.y, position.z,
        orientation.x, orientation.y, orientation.z, orientation.w)

    if msg.group == 2:
        if msg.num == 3: #[2, 3] patrol
            patrol_task(msg)

        elif msg.num == 0: #[2, 0] following
            follow_task(msg)

        else:
            print "inviled param"


def listener():
    rospy.init_node('hik_robot_test', anonymous=True)
    rospy.Subscriber("HiRobotSetTaskMsg", HikRobotSetTaskMsg, callback)
    print('hik robot task topic is ready to get req.')
    rospy.spin()

if __name__ == '__main__':
    listener()
