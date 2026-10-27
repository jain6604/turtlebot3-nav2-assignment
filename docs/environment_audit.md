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
