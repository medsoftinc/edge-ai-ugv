# Progress log

| Step | Date | What was done |
|------|------|---------------|
| 001–009 | 2026-10-19 | Environment: Distrobox Ubuntu 24.04 box, PX4 v1.17.0, Gazebo Harmonic, ROS 2 Jazzy, Micro XRCE-DDS Agent v2.4.3, QGroundControl, `px4sim` shortcut |
| Drill 1 | 2026-10-20 | QGroundControl: planned and flew an autonomous mission (takeoff → 3 waypoints → return) |
| Drill 2 | 2026-10-21 | Edited a mission (waypoint altitude 80 m), re-uploaded and flew it |
| 010 | 2026-10-21 | PX4 ↔ ROS 2 bridge: Micro XRCE-DDS Agent running, `/fmu/out/*` topics visible in ROS 2 |
| 011 | 2026-10-21 | Built `px4_msgs` (release/1.17); read live odometry from ROS 2 (z ≈ -2.97 m after takeoff, NED frame) |
| 012 | 2026-10-21 | First Python node: `scripts/ilk_dugum.py` prints the drone's altitude live |
| 013–014 | 2026-10-21 | Offboard + arm from code; drone takes off to 5 m and hovers (`scripts/kalkis.py`) |
