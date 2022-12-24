#!/usr/bin/python3

import rospy
import cv2
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image

def publish_image():
    """Capture frames from a camera and publish it to the topic image_raw
    """
    image_pub = rospy.Publisher("image_raw", Image, queue_size=10)
    bridge = CvBridge()
    capture = cv2.VideoCapture("/dev/video0")

    while not rospy.is_shutdown():
        # Capture a frame
        ret, img = capture.read()
        if not ret:
            rospy.ERROR("Could not grab a frame!")
            break

        # Publish the image to the topic image_raw
        try:
            img_msg = bridge.cv2_to_imgmsg(img, "bgr8")
            #img_msg.header.stamp = rospy.Time.now()
            image_pub.publish(img_msg)
        except CvBridgeError as error:
            print(error)


if __name__=="__main__":
    rospy.init_node("my_cam", anonymous=True)
    print("Image is being published to the topic /image_raw ...")
    publish_image()
    
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down!")
