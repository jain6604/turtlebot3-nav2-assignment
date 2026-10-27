# TurtleBot3 Nav2 Autonomous Navigation

A reproducible ROS 2 project for the Antropi Robotics software-intern assignment. It runs a TurtleBot3 Burger in the official TurtleBot3 Gazebo world and starts the official Navigation2 configuration. The supplied helper spawns a physical, laser-visible obstacle so Nav2 must update its local costmap and replan or steer around it.

## Current verification status

Project files and launch syntax have been prepared on Windows. This checkout has not yet executed Gazebo, RViz, Nav2, or the obstacle demonstration: the available WSL2 distribution is Ubuntu 26.04 with no ROS installation, while the selected stable Humble/Gazebo Classic target needs Ubuntu 22.04. No video, screenshot, navigation result, or public repository URL is claimed until those checks have run.

The target, selected for stability and upstream support, is:

| Component | Version / choice |
| --- | --- |
| Host | Ubuntu 22.04 in WSL2 with WSLg, or native Ubuntu 22.04 |
| ROS 2 | Humble Hawksbill |
| Simulator | Gazebo Classic 11 (`gazebo_ros_pkgs`) |
| Robot | TurtleBot3 Burger |
| Navigation | upstream `turtlebot3_navigation2` / Nav2 |

## Prerequisites

Use Ubuntu 22.04 and source ROS before every terminal session:

```bash
source /opt/ros/humble/setup.bash
export TURTLEBOT3_MODEL=burger
```

Install the documented dependencies and build this package:

```bash
sudo apt update
sudo apt install -y ros-humble-turtlebot3-gazebo ros-humble-turtlebot3-navigation2 \
  ros-humble-nav2-bringup ros-humble-gazebo-ros-pkgs python3-colcon-common-extensions
mkdir -p ~/tb3_ws/src
cd ~/tb3_ws/src
git clone <REPOSITORY_URL> turtlebot3-nav2-autonomous-navigation
cd ..
colcon build --symlink-install
source install/setup.bash
```

If using WSL, confirm `wsl --status` succeeds and that WSLg can open GUI applications before installing packages. A Windows-only terminal cannot run this Gazebo/RViz configuration.

## Run

Terminal 1 starts Gazebo and Nav2 (including RViz):

```bash
source /opt/ros/humble/setup.bash
source ~/tb3_ws/install/setup.bash
export TURTLEBOT3_MODEL=burger
ros2 launch turtlebot3_nav2_assignment bringup.launch.py
```

Terminal 2 adds a laser-visible cylinder after the robot has started moving toward a goal:

```bash
source /opt/ros/humble/setup.bash
source ~/tb3_ws/install/setup.bash
ros2 run turtlebot3_nav2_assignment spawn_obstacle --x 0.20 --y 1.05 --name demo_obstacle
```

In RViz, use **2D Pose Estimate** if the robot is not localized, then select **Nav2 Goal** and click a reachable goal that crosses the cylinder's vicinity. Keep **LaserScan**, **Global Costmap**, **Local Costmap**, and both paths visible. See [docs/test_protocol.md](docs/test_protocol.md) for the exact validation procedure.

## Architecture

Gazebo publishes `/clock`, `/scan`, odometry, and robot TF. `turtlebot3_navigation2` runs AMCL, planner, controller, behavior, smoother, BT navigator, and lifecycle manager. AMCL estimates `map -> odom`; the robot state publisher and Gazebo provide `odom -> base_footprint` and sensor frames. Nav2 uses the static map plus laser observations in global and local costmaps to choose and safely execute a path.

This repository deliberately delegates navigation algorithms to supported upstream packages. The assignment-specific package supplies one repeatable launch point, an SDF obstacle, and verification materials.

## Evidence and recording

Save only authentic, reviewed evidence under `screenshots/` and the final recording at `video/demo.mp4` (the MP4 is ignored by default to avoid accidentally publishing a large file). The timed narration, shot list, and checklist are in [video/](video/). Do not state that obstacle avoidance succeeded unless the actual run shows a changing local path or controller trajectory and collision-free motion.

## Troubleshooting

- `Unable to communicate with master` / no windows: source the ROS setup, check `echo $DISPLAY`, and verify WSLg or a native Ubuntu desktop.
- Lifecycle nodes do not become active: inspect `ros2 lifecycle nodes` and `ros2 lifecycle get /<node>`; confirm `use_sim_time` and `/clock`.
- Robot does not localize: set a 2D initial pose in RViz near its spawn point and ensure the map matches `turtlebot3_world`.
- Robot ignores the new obstacle: confirm `ros2 topic echo /scan --once` detects it, use a location within laser range, and watch the local costmap.

## License and attribution

The assignment glue code is MIT licensed. TurtleBot3, Gazebo, ROS 2, and Nav2 remain subject to their upstream licenses. See the upstream package documentation for their assets and configuration.
