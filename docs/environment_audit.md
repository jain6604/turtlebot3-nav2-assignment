# Initial environment audit

Date: 27 October 2026 (IST)

| Check | Result |
| --- | --- |
| Host shell | Windows PowerShell |
| Available storage | C: 162.1 GB; D: 178.9 GB; E: 182.3 GB; F: 181.5 GB free |
| Git | Installed (`2.53.0.windows.2`) |
| GitHub CLI | Installed (`2.102.0`) |
| ROS 2 / Gazebo / RViz | Not found on host PATH |
| Docker | Not found on host PATH |
| FFmpeg / OBS | Not found on host PATH |
| WSL | WSL2 works when executed outside the file sandbox; default distribution is Ubuntu 26.04.1 LTS, stopped, kernel `6.18.33.2-microsoft-standard-WSL2` |
| Ubuntu resources | 16 logical CPUs, 7.4 GiB RAM, 955 GiB free at `/` |
| GitHub authentication | `gh auth status` reports the configured token invalid; no token was displayed |

## Consequence

This machine is not currently capable of a truthful Gazebo/RViz validation or screen capture. WSL itself is available, but Ubuntu 26.04 is not the stable target selected for ROS 2 Humble/Gazebo Classic; a supported Ubuntu 22.04 WSL distribution (or a deliberately validated newer ROS/Gazebo combination) must be installed first. Publishing also requires re-authentication to GitHub. These are external authorization/administrator steps and were not bypassed.

## Follow-up implementation environment

An Ubuntu 22.04.5 WSL2 distribution named `Ubuntu-22.04-ROS` was installed at `D:\WSL\Ubuntu-22.04-ROS`; its Linux filesystem, including installed packages and the ROS workspace, is therefore on D:, not C:. ROS 2 Humble, Gazebo Classic, RViz2, TurtleBot3 Gazebo, TurtleBot3 Navigation2, Nav2 bringup, and colcon were installed. The workspace at `~/tb3_ws` built `turtlebot3_nav2_assignment` successfully.

The first integrated launch found that `turtlebot3_navigation2` requires a non-empty `params_file` when included from another launch file. The project wrapper was corrected to pass the installed Humble Burger parameter file and `use_sim_time=true`. The corrected smoke test started Gazebo, RViz, both Nav2 lifecycle managers, AMCL, map server, planner, controller, behavior, BT navigator, and costmaps. Gazebo's `/spawn_entity` service did not become available before the controlled test timeout, so the TurtleBot3 did not spawn and Nav2 lacked `odom -> base_link`. Goal completion and obstacle avoidance are consequently still **not verified**.
