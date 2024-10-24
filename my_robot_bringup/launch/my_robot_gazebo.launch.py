from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    # Path to URDF file
    urdf_path = os.path.join(
        get_package_share_directory('my_robot_description'),
        'urdf', 'my_robot.urdf.xacro'
    )

    # Launch the robot_state_publisher
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{
            'robot_description': Command(['xacro ', urdf_path])
        }]
    )

    # Include Gazebo Harmonic (ros_gz_sim) launch file
    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory('ros_gz_sim'), 'launch', 'gz_sim.launch.py')
        ])
    )

    # Spawn robot in Gazebo Harmonic using ros_gz's `create` service
    spawn_robot = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=['-name', 'my_robot', '-topic', 'robot_description'],
        output='screen'
    )

    # Launch RViz2 without configuration file
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        output='screen',
    )

    # Return the launch description
    return LaunchDescription([
        robot_state_publisher_node,
        gazebo_launch,
        spawn_robot,
        rviz_node
    ])
