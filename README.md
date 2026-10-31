# TurtleBot3 Nav2 Autonomous Navigation

A ROS 2 project developed for the Antropi Robotics Software Intern assignment. The project launches a TurtleBot3 Burger in the official Gazebo world and uses the ROS 2 Navigation2 (Nav2) stack for autonomous navigation.

The project uses upstream TurtleBot3 and Nav2 packages, with an assignment-specific launch file and a custom obstacle-spawning helper.

## Verification Status

The following functionality has been successfully verified:

- ROS 2 Humble environment and package build.
- TurtleBot3 Burger spawned in Gazebo Classic.
- Nav2 and AMCL lifecycle nodes became active.
- Planner, controller and BT Navigator became active.
- Multiple navigation goals were successfully reached.
- A custom obstacle named `demo_obstacle` was spawned in Gazebo at coordinates `(2.5, 0.0)`.
- The RViz local costmap was displayed using `/local_costmap/costmap`.

**Important:** Obstacle avoidance has not yet been conclusively demonstrated through a controlled navigation test. Obstacle spawning and local costmap visualization were verified separately from successful goal navigation.

## Technology Stack

| Component | Technology |
|---|---|
| Operating System | Ubuntu 22.04 on WSL2 |
| ROS | ROS 2 Humble |
| Simulator | Gazebo Classic 11 |
| Robot | TurtleBot3 Burger |
| Navigation | ROS 2 Navigation2 |
| Visualization | RViz2 |
| Build System | Colcon |

## Prerequisites

- Ubuntu 22.04 with ROS 2 Humble installed.
- Gazebo Classic and TurtleBot3 packages.
- Nav2 and RViz2.
- Python 3 and colcon.
- WSLg for graphical applications when using WSL2.

## Installation and Build

Source ROS 2:

```bash
source /opt/ros/humble/setup.bash
export TURTLEBOT3_MODEL=burger
```

Install the required packages if they are not already installed:

```bash
sudo apt update
sudo apt install -y ros-humble-turtlebot3-gazebo \
ros-humble-turtlebot3-navigation2 \
ros-humble-nav2-bringup \
ros-humble-gazebo-ros-pkgs \
python3-colcon-common-extensions
```

Create the workspace and clone the repository:

```bash
mkdir -p ~/robotics_ws/src
cd ~/robotics_ws/src

git clone https://github.com/jain6604/turtlebot3-nav2-assignment.git
```

Build the package:

```bash
cd ~/robotics_ws
colcon build --symlink-install
source install/setup.bash
```

## Running the Simulation

Open a terminal and run:

```bash
source /opt/ros/humble/setup.bash
source ~/robotics_ws/install/setup.bash
export TURTLEBOT3_MODEL=burger

ros2 launch turtlebot3_nav2_assignment bringup.launch.py
```

The launch file starts the TurtleBot3 Gazebo world and brings up the configured Nav2 navigation stack.

If startup is slow, increase the Nav2 startup delay:

```bash
ros2 launch turtlebot3_nav2_assignment bringup.launch.py nav2_delay:=30.0
```

## Spawning the Custom Obstacle

After the simulation has started, open another terminal:

```bash
source /opt/ros/humble/setup.bash
source ~/robotics_ws/install/setup.bash

ros2 run turtlebot3_nav2_assignment spawn_obstacle --x 2.5 --y 0.0
```

This spawns the custom demo obstacle in Gazebo.

## Autonomous Navigation

In RViz:

1. Wait for the map and robot data to load.
2. Use **2D Pose Estimate** to initialize the robot's position if necessary.
3. Select **Nav2 Goal**.
4. Click a reachable destination on the map.
5. Observe the robot's navigation and the costmap visualization.

The obstacle avoidance demonstration should be evaluated separately by confirming that the robot detects an obstacle and follows a collision-free alternative trajectory.

## Architecture

- **Gazebo:** Simulates the TurtleBot3 environment and sensors.
- **AMCL:** Estimates the robot's position on the map.
- **Nav2 Planner:** Computes a path to the navigation goal.
- **Nav2 Controller:** Executes the planned path.
- **Behavior Tree Navigator:** Coordinates the navigation task.
- **Costmaps:** Represent obstacles and environmental information for navigation.
- **RViz2:** Visualizes the robot, map, navigation status and costmaps.

The project relies on upstream ROS 2 and Nav2 algorithms rather than implementing custom navigation algorithms.

## Evidence and Documentation

The project includes documentation describing the environment, testing procedure and assignment responses.

Screenshots and the final demonstration recording are maintained separately as submission evidence. Only claim functionality that has been demonstrated and verified.

## Troubleshooting

- **Gazebo does not open:** Check ROS environment sourcing and WSLg graphical support.
- **Robot does not spawn:** Check Gazebo startup and the `/spawn_entity` service.
- **Nav2 nodes are inactive:** Inspect lifecycle states and verify simulation time.
- **Robot does not localize:** Set an initial pose using RViz's 2D Pose Estimate tool.
- **Obstacle does not appear in the costmap:** Check laser scan data, obstacle position and costmap configuration.

## License and Attribution

Assignment-specific code is provided under the MIT License. ROS 2, TurtleBot3, Gazebo and Nav2 remain subject to their respective upstream licenses.
