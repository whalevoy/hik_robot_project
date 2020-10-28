#!/usr/bin/env python

from __future__ import print_function

import sys
import rospy

from hik_robot_nav.srv import *
from std_msgs.msg import String, Header
from move_base_msgs.msg import MoveBaseGoal
from geometry_msgs.msg import PoseStamped
from hik_robot_nav.msg import HikRobotSetTaskMsg

def client_req(x, y):
    rospy.wait_for_service('hik_robot_set_task_srv')
    try:
        add_two_ints = rospy.ServiceProxy('hik_robot_set_task_srv', HikRobotSetTaskSrv)
        robot_goal = MoveBaseGoal()
        robot_goal.target_pose = PoseStamped()
        robot_goal.target_pose.header = Header()
        #robot_goal.target_pose.header.stamp = time
        robot_goal.target_pose.header.stamp = rospy.Time(12,34)
        req = HikRobotSetTaskSrvRequest(x,y,3,4,5,robot_goal)
        #resp1 = add_two_ints(x, y)
        resp = add_two_ints(req)
        return resp.result
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)



def usage():
    return "%s [x y]"%sys.argv[0]


if __name__ == "__main__":
    if len(sys.argv) == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:
        print(usage())
        sys.exit(1)

    print("test service %s+%s"%(x,y))
    print("get service resp %d "%client_req(x,y))
