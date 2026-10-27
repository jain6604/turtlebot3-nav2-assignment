# Recording shot list

1. Confirm the entire test protocol has passed; reset Gazebo and RViz to a clean initial state.
2. Arrange Gazebo and RViz side by side at readable resolution; close personal apps and notification overlays.
3. In RViz show Map, RobotModel, TF, LaserScan, Global Costmap, Local Costmap, global path, and local path.
4. Start recording with the TurtleBot3 visible in Gazebo.
5. Show RViz overlays, initialize pose if required, and send the validated goal.
6. Allow continuous autonomous motion long enough for the route to be clear.
7. Spawn the obstacle at the pre-tested coordinates and keep both its Gazebo position and RViz local costmap visible.
8. Let the behavior finish; do not cut away from a collision or failure.
9. Stop recording only after the actual terminal/result is visible.
10. Review the MP4 fully, check 60–120 seconds, resolution, legibility, and audio; then preserve it as `video/demo.mp4`.
