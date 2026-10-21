# GORİLL

**The ear hears, the eye finds, the drone follows.**

GORİLL is a drone detection and tracking system. A ground sensor hears an unauthorized drone, and an autonomous follower drone takes off, finds it with its camera and AI, and tracks it from a safe distance while recording video and position.

## How it works
1. **Ear:** An Arduino Nano RP2040 Connect on the ground recognizes drone sound with an on-device TinyML model (Edge Impulse) and sends an alarm to the ground station.
2. **Take-off:** On alarm, the follower drone (PX4) takes off and searches by rotating.
3. **Eye:** Its camera and a YOLO model (OpenVINO) detect the intruder drone.
4. **Follow:** It tracks the target from a safe distance and logs video and position.

Scope: detection and tracking only. No interception, no multi-target, no swarm, no radar.

## Tech stack
PX4 v1.17 · Gazebo Harmonic · ROS 2 Jazzy · Micro XRCE-DDS · QGroundControl · Python · YOLO · OpenVINO · Edge Impulse (TinyML) · Arduino

## Roadmap
- [x] Module 0: Setup (PX4 SITL, Gazebo, ROS 2, PX4 ↔ ROS 2 bridge)
- [ ] Module 1: Controlling the drone from code
- [ ] Module 2: Scene: camera follower drone + target, camera feed in ROS 2
- [ ] Module 3: AI: dataset, training on Colab, real-time detection with OpenVINO
- [ ] Module 4: Visual tracking + search when the target is lost
- [ ] Module 5: Acoustic early warning (Arduino) → automatic mission start
- [ ] Module 6: Integration, event log, demo video
- [ ] Module 7–9: Real hardware (Holybro X500 v2 + Pixhawk 6C, Jetson Orin Nano), field test

## Repository layout
- `scripts/`: GORİLL code (first experiments; packages will follow under `src/`)
- `ogrenme/`: learning history: Python basics and an earlier ROS 2 ground-robot exercise (publisher, subscriber, P-control)
- `PROGRESS.md`: step-by-step log of the work

## Author
Fırat Serhatlı, Software Engineering, Toros University
