#!/usr/bin/env python
import tf
import rospy
import std_msgs
import numpy as np
import geometry_msgs.msg as msg

from rover_msgs.msg import float64arrayex


def callback(data):
    datalist = data.data # 外测时间戳(ms),位置xmm,位置ymm,位置zmm,姿态rx度,姿态ry度,姿态rz度,位姿0-360度,转序 1-2-3
    timestamp = datalist[0]
    x = datalist[1] / 1000
    y = datalist[2] / 1000
    z = datalist[3] / 1000
    br = tf.TransformBroadcaster()

    br.sendTransform((x, y, z),
                     tf.transformations.quaternion_from_euler\
                         (np.deg2rad(datalist[4]), np.deg2rad(datalist[5]), np.deg2rad(datalist[6])),
                     rospy.Time.now(),
                    #  rospy.Time.from_seconds(timestamp),
                     "body",
                     "map")
    # print(data)


if __name__ == "__main__":
    rospy.init_node('lidar_pose_tf_publisher')
    subscriber = rospy.Subscriber('/pq_data', float64arrayex, callback)

    # tf_puber = tf.TransformBroadcaster()
    # tf_puber.sendTransform((x, y, z),
    #                 tf.transformations.quaternion_from_euler(),
    #                 rospy.Time.now(),
    #                 "Pandar40M_front",
    #                 "imu")
    
    rospy.spin()