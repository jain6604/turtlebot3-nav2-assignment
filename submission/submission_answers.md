# Submission Answers — Antropi Robotics

## 1. Describe your approach

I used ROS 2 Humble with the TurtleBot3 Burger simulation in Gazebo Classic and the upstream ROS 2 Navigation2 stack. I created an assignment-specific ROS 2 package containing a launch file to bring up the simulation and navigation stack, along with a custom SDF-based obstacle-spawning utility.

I configured the Burger-specific Nav2 parameters and simulation time, built the package using colcon, and tested localization and autonomous navigation through RViz.

## 2. How is autonomous navigation configured?

Gazebo provides the simulated environment, laser scan data, odometry and robot transforms. AMCL estimates the robot's position on the map, while Nav2 uses its planner, controller, behavior tree navigator and costmaps to execute navigation goals.

I verified that the relevant Nav2 lifecycle nodes became active, initialized the robot pose in RViz, and successfully sent multiple navigation goals. The navigation feedback confirmed goal completion with zero distance remaining.

## 3. How did you demonstrate obstacle handling?

I developed a custom obstacle-spawning utility that creates a physical, laser-visible cylinder in Gazebo. I successfully spawned the obstacle at the specified coordinates and verified that the local costmap was available and displayed in RViz.

A controlled test demonstrating successful collision-free obstacle avoidance has not yet been conclusively completed. The obstacle spawning and costmap visualization were verified independently.

## 4. What challenges did you face and how did you resolve them?

One of the main challenges was setting up a compatible ROS 2 development environment on Windows using Ubuntu 22.04 through WSL2. I configured ROS 2 Humble, Gazebo Classic, TurtleBot3 and Nav2.

I also encountered issues with Gazebo's entity-spawning service, environment variables and Nav2 startup configuration. I resolved the robot-spawning and configuration issues, ensured the correct TurtleBot3 Burger model was selected, and successfully brought up the simulation and navigation stack.

## 5. What did you learn from this assignment?

I gained practical experience with ROS 2, Gazebo simulation and the Nav2 navigation framework. I learned how AMCL handles localization, how Nav2 separates global planning from local control, and how costmaps represent obstacles using sensor information.

I also gained experience troubleshooting ROS 2 launch configurations, lifecycle nodes, TF transforms, simulation time and multi-terminal workflows in a WSL2 environment.

## 6. Project Links

- **GitHub Repository:** https://github.com/jain6604/turtlebot3-nav2-assignment
- **Demo Video:** To be added after recording and uploading the final demonstration.
