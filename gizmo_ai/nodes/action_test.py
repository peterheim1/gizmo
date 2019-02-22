#!/usr/bin/env python
#
# License: BSD
#   https://raw.githubusercontent.com/stonier/py_trees/devel/LICENSE
#
##############################################################################
# Documentation
##############################################################################

"""
Mocks a simple action server that rotates the robot 360 degrees.
"""

##############################################################################
# Imports
##############################################################################

import math
import py_trees_msgs.msg as py_trees_msgs
from actionlib_msgs.msg import *
from geometry_msgs.msg import Pose, Point, Quaternion, Twist
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from tf.transformations import quaternion_from_euler
from . import action_server

##############################################################################
# Classes
##############################################################################


class Rotate(action_server.ActionServer):
    """
    Simple server that controls a full rotation of the robot.

    Args:
        rotation_rate (:obj:`float`): rate of rotation )rad/s)
    """
    def __init__(self, rotation_rate=1.57):
        super(Rotate, self).__init__(action_name="rotate",
                                     action_type=py_trees_msgs.RotateAction,
                                     worker=self.worker,
                                     duration=2.0 * math.pi / rotation_rate
                                     )
        self.start()

    def worker(self):
        """
        Create some appropriate feedback.
        """
        self.action.action_feedback = 2 * math.pi * self.percent_completed / 100.0

if __name__ == '__main__':
    try:
        Rotate()
    except rospy.ROSInterruptException:
        rospy.loginfo("rotate test finished.")

