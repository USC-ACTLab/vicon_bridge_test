#!/usr/bin/env python

import rospy
from geometry_msgs.msg import TransformStamped

class MSGLatency:
    def __init__(self, source_frame, target_frame):
        self.source_frame = source_frame
        self.target_frame = target_frame
        rospy.Subscriber(target_frame, TransformStamped, self.callback)

    def callback(self, data):
        self.last_data = data

    def run(self):
        sum = 0
        count = 0
        rospy.sleep(1.0)
        while not rospy.is_shutdown():
            now = rospy.Time.now()
            t = self.last_data.header.stamp
            delta = (now - t).to_sec() * 1000 #ms
            sum += delta
            count +=1
            rospy.loginfo("Latency: %f ms (AVG: %f ms)", delta, sum / count)
            rospy.sleep(0.01)

if __name__ == '__main__':

    rospy.init_node('msg_latency', anonymous=True)
    source_frame = rospy.get_param("~source_frame", "/world")
    target_frame = rospy.get_param("~target_frame")
    msglatency = MSGLatency(source_frame, target_frame)
    msglatency.run()
