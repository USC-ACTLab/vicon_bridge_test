# vicon_bridge_test
ROS package to measure latency of the ROS vicon_bridge package

This package has several small tools to measure the latency of vicon messages.
It tries to query the latest available transformation and reports the time difference between the tf timestamp and the current time.


Sample Usage:

```
roslaunch vicon_bridge_test tf_latency_cpp.launch target_frame:=/vicon/crazyflie1/crazyflie1
```

```
roslaunch vicon_bridge_test tf_latency_py.launch target_frame:=/vicon/crazyflie1/crazyflie1
```

```
 roslaunch vicon_bridge_test msg_latency_py.launch target_frame:=/vicon/crazyflie1/crazyflie1
```
