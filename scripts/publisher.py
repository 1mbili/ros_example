#!/usr/bin/python3

import rospy
import random
from std_msgs.msg import Float64


def publisher() -> None:
    """
    Publish random float between -20 and 20 to chatter topic.

    """
    pub = rospy.Publisher('chatter', Float64, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(5)
    while not rospy.is_shutdown():
        message = random.uniform(-20, 20)
        rospy.loginfo(message)
        pub.publish(message)
        rate.sleep()


if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
