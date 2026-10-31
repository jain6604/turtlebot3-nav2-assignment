# Test protocol and evidence log

Run the commands below only after the target Ubuntu/ROS environment is installed. Record real results in the table; do not replace the placeholders with expected output.

## Preflight

```bash
source /opt/ros/humble/setup.bash
source ~/tb3_ws/install/setup.bash
export TURTLEBOT3_MODEL=burger
ros2 pkg prefix turtlebot3_gazebo
ros2 pkg prefix turtlebot3_navigation2
```

Expected: both package-prefix commands return installed paths.

## Bringup and diagnostics

Start `ros2 launch turtlebot3_nav2_assignment bringup.launch.py`. Do not start the diagnostic commands until Gazebo has had at least 45 seconds to initialize and the robot is visibly present. Then, in another terminal:

```bash
ros2 topic echo /clock --once
ros2 topic echo /scan --once
ros2 run tf2_ros tf2_echo map base_footprint
ros2 lifecycle nodes
ros2 action list | grep navigate_to_pose
```

Expected: sim time advances; `/scan` contains ranges; TF resolves; Nav2 managed nodes are listed; `navigate_to_pose` exists. For each lifecycle node, verify `active` with `ros2 lifecycle get /NODE_NAME`.

## Navigation test

1. In RViz, set **Fixed Frame** to `map` and add Map, LaserScan (`/scan`), TF, Global Costmap, Local Costmap, global path, local path, and RobotModel displays.
2. Set a 2D initial pose if necessary.
3. Send a reachable Nav2 goal in an open portion of the provided map.
4. Observe the goal, global path, controller trajectory/local path, and collision-free robot movement.
5. Capture a screenshot with RViz and Gazebo both visible.

## Obstacle-avoidance test

1. Identify an unobstructed part of the proposed route where the robot's laser can see the obstacle.
2. Begin navigation to a goal beyond that point.
3. While the robot is still at least 0.5 m from the chosen position, run:

   ```bash
   ros2 run turtlebot3_nav2_assignment spawn_obstacle --x X --y Y --name demo_obstacle
   ```

4. Confirm the red cylinder appears in Gazebo and a corresponding obstacle appears in the local costmap.
5. Record whether Nav2 changes its local plan, steers around it, waits, or reports failure. Mark success only when it reaches the goal without collision.

## Evidence record

| Check | Status | Actual output / file |
| --- | --- | --- |
| Dependencies found | PASS | Ubuntu 22.04 WSL2; ROS 2 Humble, Gazebo, RViz, TurtleBot3 and Nav2 installed |
| Gazebo robot spawn | BLOCKED | `/spawn_entity` did not become available during controlled integration test |
| Nav2 lifecycle active | PARTIAL PASS | Localization manager became active; navigation manager configured planner/controller but activation waited for missing robot TF |
| TF and scan | NOT RUN | — |
| Goal reached | NOT RUN | — |
| Obstacle avoidance | NOT RUN | — |
| Demo MP4 reviewed | NOT RUN | — |
