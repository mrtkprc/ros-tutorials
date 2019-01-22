#!/usr/bin/env python

import rospy
from std_msgs.msg import String

if __name__ == '__main__':
    #if anonymous is True, node name is composed with suffix random numbers
    rospy.init_node('robot_news_radio_transmitter',anonymous=True) #unique node name
    pub = rospy.Publisher("/robot_news_radio",String,queue_size=10) #topic_name, message type and queue size

    rate = rospy.Rate(2)
    while not rospy.is_shutdown():
        msg = String()
        msg.data = "Hi, this is Msg from Robot news Radio !"
        pub.publish(msg)
        rate.sleep()
    
    rospy.loginfo("Node was stopped")