# Technical walkthrough

## System roles

Gazebo is the physics simulator: it renders the TurtleBot3, world geometry, collision bodies, and simulated laser. RViz is only a visualization and goal-setting client; it does not drive the robot. ROS 2 nodes exchange messages through topics, services, actions, and TF.

The upstream TurtleBot3 Gazebo launch provides the robot simulation and sensor/odometry data. The upstream TurtleBot3 Navigation2 launch configures Nav2 for the matching map. This assignment package combines those supported launch files and provides a repeatable SDF obstacle for a dynamic-obstacle test.

## Frames and state estimation

The navigation chain is `map -> odom -> base_footprint -> base_link -> base_scan`.

- `map` is the fixed global map coordinate system.
- `odom` is locally smooth but can drift over long distances.
- `base_footprint` is the ground projection of the robot body.
- `base_scan` is the laser sensor frame.

Gazebo provides wheel odometry and robot transforms. AMCL compares `/scan` measurements to the static map and continuously estimates the `map -> odom` transform. This corrects odometry drift while preserving a continuous local odometry frame.

## Navigation2

Nav2 receives a goal through the `NavigateToPose` action. The BT Navigator coordinates the request. The global planner computes a route over the static/global costmap. The controller uses the local costmap, odometry, and scan data to output safe velocity commands. Recovery/behavior nodes provide structured responses when planning or progress fails. The lifecycle manager configures and activates these nodes in order.

The global costmap includes map obstacles; the local rolling costmap incorporates current laser returns. The supplied red cylinder has collision and visual geometry, so it is present in Gazebo and should produce laser data. When observed, it is marked as a local costmap obstacle; the controller can steer around it or Nav2 can replan. The correct evidence is the local-costmap change and collision-free behavior, not merely the obstacle's appearance.

## Important operating parameters

- `use_sim_time`: Nav2 must follow Gazebo `/clock`; a mismatch often prevents progress.
- Robot footprint/radius and inflation radius: these determine safe clearance.
- Laser obstacle and raytrace ranges: these limit what the costmap can mark or clear.
- AMCL initial pose: this must be close to the simulated robot's actual map position.
- Controller speed/acceleration: conservative values make recording easier but lengthen the demo.

## Limitations and improvements

This project currently wraps upstream TurtleBot3 Nav2 parameters rather than duplicating them. That reduces maintenance risk but means target-world/map compatibility must be validated during the first real run. After validation, useful follow-ups are pinning package versions, adding a recorded rosbag test, adding a custom map/world pair, and adding launch tests that assert lifecycle state.
