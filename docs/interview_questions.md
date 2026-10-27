# Interview questions and concise sample answers

## Why use Nav2 rather than write a planner from scratch?

Nav2 is the ROS 2 navigation framework used in production-style robotics stacks. The assignment asks for a working navigation system, so I configured and validated the supported framework instead of claiming that standard planning and control behavior was a novel algorithm.

## What is the difference between global and local navigation?

The global planner finds a route across the known map. The local controller executes safely in the immediate environment using odometry and live sensor data. This separation lets the robot react to obstacles that were not represented in the original map.

## Why are both `map` and `odom` needed?

Odometry is smooth locally but drifts. The map frame is globally meaningful but can be corrected abruptly by localization. AMCL supplies `map -> odom`, combining the advantages of both frames for navigation.

## How did you demonstrate avoidance?

I used a collision and laser-visible cylinder inserted on the route, observed it in the local costmap, and checked the resulting controller/local-path behavior and collision-free completion. I would report the actual outcome of that test, including a failure if Nav2 could not find a safe route.

## How do you know Nav2 is ready?

I check that `/clock`, scan, and TF are present; inspect the Nav2 action server; and verify each lifecycle-managed node reaches the `active` state before sending a goal.

## What is your next improvement?

I would make the Gazebo world and occupancy map a single versioned pair, then add an automated launch test and rosbag-based regression test for a known goal and obstacle placement.
