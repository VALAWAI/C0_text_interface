# C0 Text Interface

*This work is part of the VALAWAI human-robot interaction project based on ROS 2.*

This package is deprecated in favour of [rqt_chat](github.com/pal-robotics/rqt_chat), *a simple chat plugin for rqt, compatible with ROS4HRI.*

## Description

Text interfaces represent the simplest form of human-computer interaction, enabling users to communicate with a system through typed commands or textual inputs. This method provides a direct and efficient means of interaction. Although graphical user interfaces have emerged, offering visually intuitive experiences, text interfaces remain relevant due to their lightweight nature and simplicity. This reduced complexity allows users to focus on other aspects of the system, which is particularly advantageous during the debugging phase of a project.

Within the VALAWAI system, this component enables users to input dialogue and receive corresponding responses. Both input and output are managed via this straightforward text interface.

## Installation

Install rqt_chat and tts_msgs in a ROS 2 workspace.

```shell 
cd ws/src
git clone https://github.com/pal-robotics/rqt_chat.git
git clone https://github.com/pal-robotics/tts_msgs
# If using ROS 2 Humble
sudo apt install ros-humble-hri-msgs ros-humble-hri-actions-msgs
# If not using ROS 2 Humble
# git clone https://github.com/ros4hri/hri_msgs.git
# git clone https://github.com/ros4hri/hri_actions_msgs.git
cd ..
sudo rosdep update && sudo rosdep install --from-paths src --ignore-src -y 
```

## Usage

```shell
# after having sourced ROS
colcon build --symlink-install
source ./install/setup.bash
rqt -s rqt_chat --force-discover
```

## Topics (from the original documentation)

User messages are published as `hri_msgs/msg/LiveSpeech` messages on the `/humans/voices/anonymous_speaker/speech` topic.

TTS action call to `/tts_engine/tts` (`tts_msgs/action/TTS`) are then displayed as robot's messages.
