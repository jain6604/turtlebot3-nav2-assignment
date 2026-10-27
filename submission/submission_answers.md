# Submission answers — draft pending live validation

These answers are intentionally conservative. Replace only the bracketed fields after the real run, and use the actual repository and video URLs.

## Describe your approach

I used ROS 2 Humble with the supported TurtleBot3 Burger Gazebo simulation and the upstream TurtleBot3 Navigation2 stack. I created a small assignment package that launches the simulator and Nav2 together, plus an SDF-based obstacle tool to make the local-obstacle test repeatable. I used RViz to inspect localization, laser data, paths, and costmaps and to send a `NavigateToPose` goal.

## How is autonomous navigation configured?

Gazebo provides `/clock`, odometry, transforms, and laser data. AMCL localizes the robot on the map, and Nav2's planner, controller, behavior tree navigator, recovery behaviors, and lifecycle manager handle the goal. I verified [ACTUAL VERIFIED ITEMS ONLY: lifecycle state / TF / scan / goal completion].

## How did you demonstrate obstacle handling?

During an active navigation run, I spawned a red cylinder with collision and laser geometry on the route. I checked that it appeared in the local costmap and observed [ACTUAL REACTION]. The final result was [ACTUAL RESULT].

## Challenge and resolution

The preparation environment was Windows-only with no ROS/Gazebo installation, and its WSL invocation returned `Wsl/E_ACCESS_DENIED`. I did not claim an untested simulation as complete. I prepared the versioned ROS package and validation checklist, then [ACTUAL RESOLUTION AFTER IT OCCURS].

## Key learning

I learned how Nav2 separates global map-based planning from local sensor-driven control, why AMCL publishes the `map -> odom` correction, and how local costmaps turn live laser observations into avoidance constraints.

## Links

- Repository: [PENDING — authenticate GitHub and publish]
- Demo video: [PENDING — record and review a genuine run]
