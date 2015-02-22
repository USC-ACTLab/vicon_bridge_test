#include <ros/ros.h>
#include <tf/transform_listener.h>

int main(int argc, char** argv) {
  ros::init(argc, argv, "tf_latency");
  ros::NodeHandle node("~");

  std::string source_frame = "/world";
  std::string target_frame;
  node.getParam("target_frame", target_frame);

  // Reducing the cache size from 10 seconds to any other value doesn't seem to change anything
  tf::TransformListener listener(ros::Duration(0.02));

  listener.waitForTransform(source_frame, target_frame, ros::Time(0), ros::Duration(5.0));
  float sum = 0;
  int count = 0;

  while (node.ok()) {
    ros::Time now = ros::Time::now();
    ros::Time t;
    listener.getLatestCommonTime(source_frame, target_frame, t, NULL);
    float delta = (now - t).toSec() * 1000; //ms
    sum += delta;
    count +=1;
    ROS_INFO("Latency: %f ms (AVG: %f ms)", delta, sum / count);

    // Clearing the buffer reduces the latency, however can cause that there is no transformation available in the next iteration
    //listener.clear();

    ros::Duration(0.01).sleep();
  }

  return 0;
}
