#!/usr/bin/env python
import copy
import sys
import rospy
import moveit_commander
import geometry_msgs.msg
from geometry_msgs.msg import Point, Pose
from moveit_msgs.msg import MoveGroupActionFeedback
import moveit_msgs.msg
from std_msgs.msg import Int8

from math import pi
scale = 1.0
class trajectory:
    # Initialize class
    def __init__(self):
        # setup movie commander
        moveit_commander.roscpp_initialize(sys.argv)
        # setup robot, scene, and move group
        self.robot = moveit_commander.RobotCommander()
        self.scene = moveit_commander.PlanningSceneInterface()
        self.group = moveit_commander.MoveGroupCommander('manipulator')
        # setup some configs
        self.group.set_goal_position_tolerance(0.05)
        #self.group.set_planner_id('RRTConnectkConfigDefault')
        self.group.set_planning_time(5)
        self.group.set_num_planning_attempts(5)
        # set status to ready
        self.status = 0

        rob = moveit_commander.RobotCommander()
        print("============ Printing robot state")
        print(rob.get_current_state())
        print("")

        print("============ Available Planning Groups:", rob.get_group_names())

        joint_goal = self.group.get_current_joint_values()
        print(joint_goal[0]) 
        print(joint_goal[1])
        print(joint_goal[2]) 
        print(joint_goal[3])
        print(joint_goal[4]) 
        print(joint_goal[5])
        
        # group_name = "manipulator"
        # move_group = moveit_commander.MoveGroupCommander(group_name)
        # pose_target = geometry_msgs.msg.Pose()
        # print(pose_target.position.x)
        # print(pose_target.position.y) 
        # print(pose_target.position.z)
        # pose_goal = geometry_msgs.msg.Pose()
        # pose_goal.orientation.w = 1.0
        # pose_goal.position.x = 0.488
        # pose_goal.position.y = 0.109
        # pose_goal.position.z = -0.473

        # move_group.set_pose_target(pose_goal)
        # # `go()` returns a boolean indicating whether the planning and execution was successful.
        # success = move_group.go(wait=True)
        # # Calling `stop()` ensures that there is no residual movement
        # move_group.stop()
        # # It is always good to clear your targets after planning with poses.
        # # Note: there is no equivalent function for clear_joint_value_targets().
        # move_group.clear_pose_targets()
        # waypoints = []

        # wpose = move_group.get_current_pose().pose
        # wpose.position.z -= scale * 0.1  # First move up (z)
        # wpose.position.y += scale * 0.2  # and sideways (y)
        # waypoints.append(copy.deepcopy(wpose))

        # wpose.position.x += scale * 0.1  # Second move forward/backwards in (x)
        # waypoints.append(copy.deepcopy(wpose))

        # wpose.position.y -= scale * 0.1  # Third move sideways (y)
        # waypoints.append(copy.deepcopy(wpose))

        # # We want the Cartesian path to be interpolated at a resolution of 1 cm
        # # which is why we will specify 0.01 as the eef_step in Cartesian
        # # translation.  We will disable the jump threshold by setting it to 0.0,
        # # ignoring the check for infeasible jumps in joint space, which is sufficient
        # # for this tutorial.
        # (plan, fraction) = move_group.compute_cartesian_path(
        #     waypoints, 0.01, 0.0  # waypoints to follow  # eef_step
        # )  # jump_threshold

        # # Note: We are just planning, not asking move_group to actually move the robot yet:
        # return plan, fraction


        # move_group.execute(plan, wait=True)

        # joint_goal[0] = 0.6840646803337611
        # joint_goal[1] = -0.8614314508493033
        # joint_goal[2] = 0.3673292038379259
        # joint_goal[3] = -2.4828628044143306
        # joint_goal[4] = 0.3039265950207728
        # joint_goal[5] = 0.0000443833493850
       

        # # The go command can be called with joint values, poses, or without any
        # # parameters if you have already set the pose or joint target for the group
        # self.group.go(joint_goal, wait=True)

        joint_goal = self.group.get_current_joint_values()

        joint_goal[0] =  0.29571830982448866     
        joint_goal[1] =  -1.8063344655060094
        joint_goal[2] =  1.4084949864563407    
        joint_goal[3] = -2.6670513959199793
        joint_goal[4] =  0.6896895248473998       
        joint_goal[5] = 0.09834087292624538

        self.group.go(joint_goal, wait=True)


        # joint_goal = self.group.get_current_joint_values()

        # joint_goal[0] =  0.3962795161911732     
        # joint_goal[1] =  -1.6298009530058497
        # joint_goal[2] =  2.151127558836862   
        # joint_goal[3] = -3.645166943261462
        # joint_goal[4] =  0.5825268945772235      
        # joint_goal[5] = -0.14878288716097554
        
        self.group.go(joint_goal, wait=True)
        # Calling ``stop()`` ensures that there is no residual movement
        self.group.stop()


if __name__=='__main__':
    rospy.init_node('Trajecory_UR3')
    trajectory()
    try:
        rospy.spin()
    except rospy.ROSInterruptException:
        pass