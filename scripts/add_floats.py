#!/usr/bin/python3

from __future__ import print_function

from ros_example.srv import AddTwoFloats, AddTwoFloatsResponse
import rospy

def handle_add_two_floats(req):
    print("Returning [%s + %s = %s]"%(req.a, req.b, (req.a + req.b)))
    return AddTwoFloatsResponse(req.a + req.b)

def add_two_ints_server():
    rospy.init_node('add_two_floats_server')
    s = rospy.Service('add_two_floats', AddTwoFloats, handle_add_two_floats)
    print("Ready to add two floats.")
    rospy.spin()

if __name__ == "__main__":
    add_two_ints_server()