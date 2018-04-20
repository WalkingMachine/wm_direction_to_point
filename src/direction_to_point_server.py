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
        print("wm_direction_to_point is ready")
        rospy.spin()

    def service(self, req):

        point = geometry_msgs.msg.PointStamped()
        point.header.frame_id = "map"
        point.point = req.point
        self.listener.waitForTransform("map", req.origine, rospy.Time(0), rospy.Duration(1))
        print("Frame : map")
        print(" point : "+str(point.point))
        point = self.listener.transformPoint(req.origine, point)

        RefPoint = geometry_msgs.msg.PointStamped()
        RefPoint.header.frame_id = req.reference
        self.listener.waitForTransform(req.reference, req.origine, rospy.Time(0), rospy.Duration(1))
        print("RefFrame : "+req.reference)
        print(" RefPoint : "+str(RefPoint.point))
        RefPoint = self.listener.transformPoint(req.origine, RefPoint)

        print("OriginFrame : "+req.origine)
        print(" point : "+str(point.point))
        print(" RefPoint : "+str(RefPoint.point))

        yaw = math.atan2((point.point.y - RefPoint.point.y), (point.point.x - RefPoint.point.x))
        dist = ((point.point.y - RefPoint.point.y)**2+(point.point.x - RefPoint.point.x)**2)**0.5
        pitch = math.atan2((point.point.z - RefPoint.point.z), dist)

        return get_directionResponse(yaw, pitch )

if __name__ == "__main__":
    Frames()
