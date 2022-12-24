#!/usr/bin/python3

import rospy
import cv2
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image

def callback(image_msg):
    """This function is called to handle the subscribed messages

    Args:
        image_msg (Image): message type Image from sensor_msgs
    """
    try:
        cv_image = bridge.imgmsg_to_cv2(image_msg)
        cv2.imshow('ROS Image Subscriber', cv_image)
        cv2.waitKey(10)
    except CvBridgeError as error:
        print(error)

if __name__=="__main__":
    bridge = CvBridge()
    rospy.init_node("image_subscriber", anonymous=True)
    print("Subscribe images from topic /image_raw ...")

    image_subcriber = rospy.Subscriber("image_raw", Image, callback)
    
    try:
        # spin() simply keeps python from exiting until this node is stopped
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down!")
