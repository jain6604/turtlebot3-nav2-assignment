# Timed demo narration (use only after real validation)

Target duration: 100 seconds. Replace bracketed results with observed facts before recording; do not narrate unverified behavior.

| Time | Visible | Narration and action |
| --- | --- | --- |
| 0–10 s | Gazebo world, robot, obstacles | “This is my TurtleBot3 Burger autonomous-navigation simulation using ROS 2 Humble, Gazebo, and Navigation2.” Keep the robot and surrounding geometry in view. |
| 10–25 s | Gazebo then RViz | “Gazebo provides physics, odometry, and the laser scan. In RViz, the static map and AMCL localization place the robot in the global map frame.” Switch to RViz. |
| 25–40 s | RViz map, robot, scan, paths, costmaps | “Nav2 combines a global planner with a local controller. The global costmap represents known map obstacles, while the local costmap is updated from the laser.” Point out each display. |
| 40–65 s | Send goal and moving robot | “I send a Nav2 goal beyond the open area. The planner produces the blue global route, and the robot follows it autonomously.” Set the goal and allow quiet motion. |
| 65–85 s | Red obstacle, local costmap and changed path | “A laser-visible obstacle is now introduced on the route. It appears in the local costmap, and Nav2 [describe observed reaction: steers/replans/stops safely].” Spawn obstacle only after the goal is underway. |
| 85–100 s | Goal/result status and Gazebo | “The robot [actual final result]. This demonstrates the ROS 2 navigation pipeline from localization through planning, control, and live obstacle handling.” Show final robot position and goal status. |
