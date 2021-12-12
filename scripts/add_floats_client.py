#!/usr/bin/python3

from __future__ import print_function

import sys
import rospy
from ros_example.srv import *

def add_two_floats_client(id : str, x : float, y : float) -> float:
    """
    Wait for a client request and add two floats numbers
    
    Args:
    -------
     - `id` : Client request id
     - `x` : first float to add
     - `y` : second float to add    
    
    Returns:
    ---------
    - Calculated Value. Sum of 2 floats.
    
    """
    
    rospy.wait_for_service('add_two_floats')
    try:
        add_two_floats = rospy.ServiceProxy('add_two_floats', AddTwoFloats)
        resp1 = add_two_floats(id, x, y)
        return resp1.sum
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def usage() -> str:
    """
    Shows how data have to be given in input
     
    Returns:
    ---------
    - Returns format in which data should be given in input
    """
    return "%s [id x y]"%sys.argv[0]

def validateInput() -> bool:
    """
    Validates if the input is length 4

    Returns:
    ---------
    Prints usage and exit from program
    """
    if len(sys.argv) != 4:
        print(usage())
        sys.exit(1)
    

if __name__ == "__main__":
    validateInput()
    id = sys.argv[1]
    x = float(sys.argv[2])
    y = float(sys.argv[3])
    print("Requesting %s+%s"%(x, y))
    print("Operation ID = %s, %s + %s = %s"%(id, x, y, add_two_floats_client(id, x, y)))