# Test Protocol and Evidence Log

This document records the setup, validation procedure, observed results and evidence for the Antropi Robotics TurtleBot3 Nav2 assignment.

Only tests actually performed are marked as passed.

## 1. Environment

- Operating System: Ubuntu 22.04 on WSL2
- ROS 2: Humble
- Simulator: Gazebo Classic 11
- Robot: TurtleBot3 Burger
- Navigation: ROS 2 Navigation2
- Visualization: RViz2
- Workspace: `~/robotics_ws`

## 2. Preflight

Source the ROS environment:

```bash
source /opt/ros/humble/setup.bash
source ~/robotics_ws/install/setup.bash
export TURTLEBOT3_MODEL=burger
```

Check installed packages:

```bash
ros2 pkg prefix turtlebot3_gazebo
ros2 pkg prefix turtlebot3_navigation2
ros2 pkg prefix turtlebot3_nav2_assignment
```

The package build completed successfully using:

```bash
cd ~/robotics_ws
colcon build --symlink-install
```

## 3. Bringup and Diagnostics

The Gazebo simulation was launched using the TurtleBot3 world. The Nav2 navigation stack was subsequently started with the Humble Burger configuration and simulation time enabled.

The following functionality was verified:

- TurtleBot3 Burger spawned successfully in Gazebo.
- `/clock`, `/scan`, `/odom` and robot TF data were available.
- AMCL became active.
- BT Navigator, Controller Server and Planner Server became active.
- The `map` to `odom` transform was successfully resolved.
- Navigation costmap topics were available.

## 4. Navigation Test

The following procedure was performed in RViz:

1. Loaded the map and initialized the robot pose using 2D Pose Estimate.
2. Verified that localization and navigation components were active.
3. Sent reachable navigation goals using Nav2 Goal.
4. Observed navigation feedback.

**Observed result:** Multiple navigation goals were successfully reached. The navigation feedback showed `reached`, distance remaining `0.00 m`, and zero recoveries.

## 5. Custom Obstacle and Costmap Test

The assignment-specific obstacle helper was executed:

```bash
ros2 run turtlebot3_nav2_assignment spawn_obstacle --x 2.5 --y 0.0
```

**Observed result:**

- The helper reported successful spawning of `demo_obstacle` at `(2.50, 0.00)`.
- The obstacle appeared in the Gazebo Models panel.
- The local costmap topic `/local_costmap/costmap` was available.
- The local costmap was successfully displayed in RViz.

**Important limitation:** A controlled test demonstrating the robot changing its trajectory and successfully avoiding the spawned obstacle has not yet been conclusively completed. Obstacle spawning and costmap visualization must not be treated as proof of successful obstacle avoidance.

## 6. Obstacle-Avoidance Test Procedure

To complete the remaining validation:

1. Identify a reachable navigation route that passes near the obstacle.
2. Send a goal beyond the obstacle.
3. Spawn the obstacle at a suitable position along the route, within the robot's sensor range.
4. Observe the LaserScan and local costmap.
5. Check whether the controller changes its trajectory or Nav2 replans.
6. Confirm the robot reaches the goal without colliding with the obstacle.

Mark this test as passed only after observing successful collision-free avoidance.

## 7. Evidence Log

| Check | Status | Evidence |
|---|---|---|
| ROS 2 and package build | PASS | Successful colcon build |
| Gazebo robot spawn | PASS | `01_gazebo_obstacle.png` |
| Nav2 lifecycle activation | PASS | RViz navigation screenshot |
| AMCL localization | PASS | Active lifecycle state |
| TF availability | PASS | `map` to `odom` transform resolved |
| Navigation goals | PASS | `02_rviz_navigation_reached.png` |
| Custom obstacle spawning | PASS | `01_gazebo_obstacle.png` |
| Local costmap visualization | PASS | `03_rviz_local_costmap.png` |
| Controlled obstacle avoidance | PENDING | Not conclusively demonstrated |
| Final demo video | PENDING | To be recorded |

## 8. Troubleshooting

- If Gazebo does not open, source ROS 2 and check WSLg graphical support.
- If `/spawn_entity` is unavailable, allow Gazebo to initialize fully.
- If Nav2 nodes remain inactive, inspect lifecycle states and simulation time.
- If localization fails, initialize the robot pose using RViz 2D Pose Estimate.
- If an obstacle does not appear in the costmap, inspect LaserScan data and obstacle position.

## 9. Submission Evidence

The following screenshots have been captured:

- `01_gazebo_obstacle.png`
- `02_rviz_navigation_reached.png`
- `03_rviz_local_costmap.png`

The final 1–2 minute Gazebo and RViz demonstration video remains to be recorded.

