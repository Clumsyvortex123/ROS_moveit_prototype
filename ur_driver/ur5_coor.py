#!/usr/bin/env python
import copy
from os import wait
from shutil import move 
import sys
import rospy
import moveit_commander
import geometry_msgs.msg
import moveit_msgs.msg
from std_msgs.msg import Int8
from math import pi

scale = 1.0

class trajectory :
    def __init__(self):
        #setup commander
        moveit_commander.roscpp_initialize(sys.argv)

        #setup scene for robot
        self.robot = moveit_commander.RobotCommander()
        self.scene = moveit_commander.PlanningSceneInterface()
        self.group = moveit_commander.MoveGroupCommander('manipulator')
        
        #configuration setup
        self.group.set_goal_position_tolerance(0.05)

        #self.group.set_planner_id('RRTConnectkConfigDefault')

        self.group.set_planning_time(5)
        self.group.set_num_planning_attempts(5)

        #applying ready status
        self.status = 0


 #-------------------------------------------------------------------------------------
 # joint based goal and poition scrpit
        joint_goal =self.group.get_current_joint_values()   #gets all current joint vector values in array format
        print(joint_goal[0]) #obtain joint position vector data
        print(joint_goal[1])
        print(joint_goal[2]) 
        print(joint_goal[3])
        print(joint_goal[4]) 
        print(joint_goal[5])

        #user inout joint values
        joint_goal[0] = float(input("enter joint 0: "))    
        joint_goal[1] = float(input("enter joint 1: "))  
        joint_goal[2] = float(input("enter joint 2: "))      
        joint_goal[3] = float(input("enter joint 3: "))  
        joint_goal[4] = float(input("enter joint 4: "))         
        joint_goal[5] = float(input("enter joint 5: ")) 

        self.group.go(joint_goal,wait =True) 
        self.group.stop() 

#-------------------------------------------------------------------------------------
 # pose coordinates based goal and poition scrpit        

        




if __name__=='__main__':
    rospy.init_node('Trajecory_UR3')
    while True:
        trajectory()
        group_name = "manipulator"
        move_group = moveit_commander.MoveGroupCommander(group_name)
        wpose = move_group.get_current_pose().pose
        print(wpose)

    try:
        rospy.spin()
    except rospy.ROSInterruptException:
        pass