# Resume checklist — live validation and publication

Prepared on 27 October 2026. Use this checklist only after privileged WSL access is available again.

## 1. Resolve Gazebo spawn service

The current wrapper successfully starts Gazebo and Nav2, but `/spawn_entity` was absent during the controlled smoke test. Start the system and wait at least 45 seconds before concluding the factory service is unavailable:

```bash
source /opt/ros/humble/setup.bash
source ~/tb3_ws/install/setup.bash
export TURTLEBOT3_MODEL=burger
ros2 launch turtlebot3_nav2_assignment bringup.launch.py
```

In a second terminal:

```bash
source /opt/ros/humble/setup.bash
ros2 service list | grep spawn_entity
ros2 node list
```

If `spawn_entity` is absent, inspect the latest Gazebo log under `~/.ros/log/` and verify the gzserver command includes `libgazebo_ros_factory.so`. Do not proceed to recording until the robot is visible in Gazebo and `/odom`, `/scan`, and TF are live.

## 2. Verify navigation

Run every command in [test_protocol.md](test_protocol.md). Mark a test passed only with actual terminal output or a captured screenshot. Set the initial pose in RViz before sending a goal if AMCL does not localize automatically.

## 3. Verify obstacle behavior

Use a pre-tested coordinate on the actual planned route:

```bash
ros2 run turtlebot3_nav2_assignment spawn_obstacle --x X --y Y --name demo_obstacle
```

Confirm: the red cylinder appears in Gazebo; the laser sees it; the local costmap changes; the local path/controller safely reacts; and the robot reaches the goal without contact. If a test fails, record the factual result and adjust the world/goal/obstacle position rather than claiming avoidance.

## 4. Capture evidence and record

Save reviewed screenshots under `screenshots/` and record your own final run using [video_script.md](../video/video_script.md), [video_shot_list.md](../video/video_shot_list.md), and [video_checklist.md](../video/video_checklist.md).

## 5. Publish only after validation

Authenticate interactively with GitHub CLI, then create a public repository, push the commits, and verify the public URL. Replace the pending links in [submission_answers.md](../submission/submission_answers.md) with the actual repository and video locations. Do not upload `video/demo.mp4` by default unless you intentionally choose a hosting method and verify its size/accessibility.

## External blockers as of this revision

- The Codex environment has rejected further privileged WSL/Git commands because its approval service has reached its usage limit.
- The saved GitHub CLI token was previously reported invalid, so interactive re-authentication is required before publication.
