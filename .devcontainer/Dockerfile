FROM dorowu/ubuntu-desktop-lxde-vnc:focal as base
# FROM ros:galactic-ros-core-focal as base


ARG DEBIAN_FRONTEND=noninteractive
RUN echo "Set disable_coredump false" >> /etc/sudo.conf
RUN apt-get update -q && \
    apt-get upgrade -yq && \
    apt-get install -yq wget curl git build-essential vim sudo lsb-release locales bash-completion tzdata gosu && \
    rm -rf /var/lib/apt/lists/*
RUN useradd --create-home --home-dir /home/ubuntu --shell /bin/bash --user-group --groups adm,sudo ubuntu && \
    echo ubuntu:ubuntu | chpasswd && \
    echo "ubuntu ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
ENV USER ubuntu
ARG DEBIAN_FRONTEND=

ENV ROS_DISTRO=galactic
ENV AMENT_PREFIX_PATH=/opt/ros/${ROS_DISTRO}
ENV COLCON_PREFIX_PATH=/opt/ros/${ROS_DISTRO}
ENV LD_LIBRARY_PATH=/opt/ros/${ROS_DISTRO}/lib
ENV PATH=/opt/ros/${ROS_DISTRO}/bin:$PATH
ENV PYTHONPATH=/opt/ros/${ROS_DISTRO}/lib/python3.8/site-packages
ENV ROS_PYTHON_VERSION=3
ENV ROS_VERSION=2

RUN apt-get update && apt-get install -y \
    curl \
    gnupg2 \
  && curl http://repo.ros2.org/repos.key | apt-key add - \
  && sh -c 'echo "deb [arch=amd64,arm64] http://packages.ros.org/ros2/ubuntu `lsb_release -cs` main" > /etc/apt/sources.list.d/ros2-latest.list' \
  && apt-get update && apt-get install -y \
    ros-${ROS_DISTRO}-desktop \
    ros-${ROS_DISTRO}-gazebo* \
    python3-argcomplete \
    python3-colcon-common-extensions \
    python3-colcon-mixin \
  && rm -rf /var/lib/apt/lists/*


# install bootstrap tools
RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential \
    git \
    python3-rosdep \
    python3-vcstool \
    && rm -rf /var/lib/apt/lists/*

# bootstrap rosdep
RUN rosdep init && \
  rosdep update --rosdistro $ROS_DISTRO

# setup colcon mixin and metadata
RUN colcon mixin add default \
      https://raw.githubusercontent.com/colcon/colcon-mixin-repository/master/index.yaml && \
    colcon mixin update && \
    colcon metadata add default \
      https://raw.githubusercontent.com/colcon/colcon-metadata-repository/master/index.yaml && \
    colcon metadata update

# install ros2 packages
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     ros-${ROS_DISTRO}-desktop \
#     ros-${ROS_DISTRO}-gazebo* \
#     && rm -rf /var/lib/apt/lists/* \
#     && rosdep init || echo "rosdep already initialized"

RUN apt-get update && apt-get install -y\
    python3-colcon-common-extensions\
    ros-${ROS_DISTRO}-cartographer\
    ros-${ROS_DISTRO}-cartographer-ros \
    ros-${ROS_DISTRO}-navigation2 \
    ros-${ROS_DISTRO}-nav2-bringup \
    python3-vcstool \
    && rm -rf /var/lib/apt/lists/*


RUN apt-get update \
  && echo "source /usr/share/bash-completion/completions/git" >> /home/$USER/.bashrc \
  && echo "if [ -f /opt/ros/${ROS_DISTRO}/setup.bash ]; then source /opt/ros/${ROS_DISTRO}/setup.bash; fi" >> /home/$USER/.bashrc \
  && echo "cd /workspaces/DevDays" >> /home/$USER/.bashrc \
  && echo 'export PS1="\[\e[31m\][\[\e[m\]\[\e[38;5;172m\]\u\[\e[m\]@\[\e[38;5;153m\]\h\[\e[m\]\[\e[38;5;214m\]\W\[\e[m\]\[\e[31m\]]\[\e[m\]\\$"' >> /home/$USER/.bashrc

COPY "./" "/workspaces/DevDays"
COPY "/entrypoint.sh" "/entrypoint.sh"
ENTRYPOINT ["/entrypoint.sh"]
