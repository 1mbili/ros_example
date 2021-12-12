#!/usr/bin//python3

import rospy
import numpy as np
from std_msgs.msg import Float64
a = []


def callback(data: float) -> None:
    """
    Append received data to array and then calculate l2 norm of an array. Then print new l2 norm as rospy loginfo.

    Args:
    -----
    - `data`: float64 value, recived from a subscribed topic
    """
    a.append(data.data)
    norm = np.linalg.norm(a, 2)
    rospy.loginfo(rospy.get_caller_id() + " Array l2 form: %.4f", norm)


def listener() -> None:
    """
    Initialize rospy node and subscribe to "chatter" topic.

    """
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("chatter", Float64, callback)

    rospy.spin()


if __name__ == '__main__':
    listener()
