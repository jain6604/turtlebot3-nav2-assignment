# Submission answers — draft pending live validation

These answers are intentionally conservative. Replace only the bracketed fields after the real run, and use the actual repository and video URLs.

## Describe your approach

I used ROS 2 Humble with the supported TurtleBot3 Burger Gazebo simulation and the upstream TurtleBot3 Navigation2 stack. I created a small assignment package that launches the simulator and Nav2 together, plus an SDF-based obstacle tool to make the local-obstacle test repeatable. The package built successfully, and the controlled bring-up started Gazebo, RViz, AMCL, map serving, and the core Nav2 components. I will only state that I inspected robot telemetry or sent a `NavigateToPose` goal after the robot-spawn test is complete.

## How is autonomous navigation configured?

Gazebo provides `/clock`, odometry, transforms, and laser data. AMCL localizes the robot on the map, and Nav2's planner, controller, behavior tree navigator, recovery behaviors, and lifecycle manager handle the goal. I verified that the map server, AMCL, planner, controller, behavior server, BT navigator, and costmaps launched; [ADD ACTUAL VERIFIED TF / SCAN / GOAL RESULTS AFTER THE FINAL RUN].

## How did you demonstrate obstacle handling?

The project includes a red cylinder with collision and laser geometry and a repeatable ROS 2 spawn helper. The final demonstration is pending robot-spawn recovery; after that run, I will report only the observed local-costmap response and final goal result.

## Challenge and resolution

The initial machine had no ROS environment. I installed the supported Ubuntu 22.04/ROS 2 Humble toolchain onto a D:-backed WSL distribution, built the package, and found that the upstream Nav2 launch needs an explicit Burger parameter file when included by another launch file. I corrected that wrapper configuration. The remaining issue is Gazebo factory-service readiness, which I am diagnosing before claiming robot motion or obstacle avoidance.

## Key learning

I learned how Nav2 separates global map-based planning from local sensor-driven control, why AMCL publishes the `map -> odom` correction, and how local costmaps turn live laser observations into avoidance constraints.

## Links

- Repository: [PENDING — authenticate GitHub and publish]
- Demo video: [PENDING — record and review a genuine run]
