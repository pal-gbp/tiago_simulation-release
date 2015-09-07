Name:           ros-indigo-tiago-hardware-gazebo
Version:        0.0.1
Release:        0%{?dist}
Summary:        ROS tiago_hardware_gazebo package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       gazebo-devel
Requires:       ros-indigo-control-toolbox
Requires:       ros-indigo-gazebo-ros-control
Requires:       ros-indigo-hardware-interface
Requires:       ros-indigo-joint-limits-interface
BuildRequires:  gazebo-devel
BuildRequires:  ros-indigo-angles
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-control-toolbox
BuildRequires:  ros-indigo-gazebo-ros-control
BuildRequires:  ros-indigo-hardware-interface
BuildRequires:  ros-indigo-joint-limits-interface

%description
Gazebo plugin to control a Tiago robot in simulation.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Sep 07 2015 PAL Robotics <maintainer@pal-robotics.com> - 0.0.1-0
- Autogenerated by Bloom

