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
| WSL | Windows executable present, but `wsl --status` and `wsl -l -v` returned `Wsl/E_ACCESS_DENIED` |
| GitHub authentication | `gh auth status` reports the configured token invalid; no token was displayed |

## Consequence

This machine is not currently capable of a truthful Gazebo/RViz validation or screen capture. Installing and running the selected Ubuntu/ROS stack requires that the owner restore WSL access (or provide an Ubuntu workstation). Publishing also requires re-authentication to GitHub. These are external authorization/administrator steps and were not bypassed.
