#!/usr/bin/env python

import rospy
import tf
import tf2_ros
import tf2_msgs.msg
import geometry_msgs.msg
import math
import roslib
from wm_direction_to_point.srv import get_direction, get_directionResponse




class Frames():

    def __init__(self):
        rospy.init_node('wm_direction_to_point')
        s = rospy.Service('get_direction', get_direction, self.service)
        self.listener = tf.TransformListener()
        self.broadcaster = tf.TransformBroadcaster()
        rospy.spin()
#njnvd
    def service(self, req):
        print(req.reference)

        x = req.point.x
        y = req.point.y
        z = req.point.z

        print (x, y, z)
        self.broadcaster.sendTransform((x, y, z),
                                  tf.transformations.quaternion_from_euler(0, 0, 0),
                                  rospy.Time.now(),
                                  "point",
                                  "map")

        self.listener.waitForTransform("point", req.origine, rospy.Time(0), rospy.Duration(1))
        (trans, rot) = self.listener.lookupTransform("point", req.origine, rospy.Time(0))
        self.listener.waitForTransform(req.reference, req.origine, rospy.Time(0), rospy.Duration(1))
        (trans2, rot) = self.listener.lookupTransform(req.reference, req.origine, rospy.Time(0))

        angular = math.atan2((trans[1] - trans2[1]), (trans[0] - trans2[0]))

        print('angle = ' + str(angular))

        return get_directionResponse(angular, 0 )

if __name__ == "__main__":
    Frames()
