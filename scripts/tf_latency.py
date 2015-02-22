#!/usr/bin/env python

import rospy
from tf import TransformListener

class TFLatency:
    def __init__(self, source_frame, target_frame):
        self.source_frame = source_frame
        self.target_frame = target_frame
        self.listener = TransformListener(1, rospy.Duration(0.01))

    def run(self):
        self.listener.waitForTransform(self.source_frame, self.target_frame, rospy.Time(), rospy.Duration(5.0))
        sum = 0
        count = 0
        while not rospy.is_shutdown():
            now = rospy.Time.now()
            if self.listener.canTransform(self.source_frame, self.target_frame, rospy.Time(0)):
                t = self.listener.getLatestCommonTime(self.source_frame, self.target_frame)
                delta = (now - t).to_sec() * 1000 #ms
                sum += delta
                count +=1
                rospy.loginfo("Latency: %f ms (AVG: %f ms)", delta, sum / count)
                #if delta > 20:
                #    self.listener.clear()
            rospy.sleep(0.01)

if __name__ == '__main__':

    rospy.init_node('tf_latency', anonymous=True)
    source_frame = rospy.get_param("~source_frame", "/world")
    target_frame = rospy.get_param("~target_frame")
    tflatency = TFLatency(source_frame, target_frame)
    tflatency.run()
