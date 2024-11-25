import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():

   pkg_ros_gz_sim = get_package_share_directory('ros_gz_sim')
   pkg_diff_robot_custom_world = get_package_share_directory('diff_robot_custom_world')

   world_file = os.path.join(pkg_diff_robot_custom_world, 'worlds', 'my_world.sdf')

   gz_sim = IncludeLaunchDescription(
       PythonLaunchDescriptionSource(
           os.path.join(pkg_ros_gz_sim, 'launch', 'gz_sim.launch.py')),
       launch_arguments={
           'gz_args': '-r ' + world_file
       }.items(),
   )

   rviz_node = Node(
       package='rviz2',
       executable='rviz2',
       output='screen',
   )

   bridge = Node(
       package='ros_gz_bridge',
       executable='parameter_bridge',
       arguments=[
           '/model/vehicle/cmd_vel@geometry_msgs/msg/Twist@gz.msgs.Twist',
           '/model/vehicle/odometry@nav_msgs/msg/Odometry@gz.msgs.Odometry',
       ],
       parameters=[{
           'qos_overrides./model/vehicle.subscriber.reliability': 'reliable',
       }],
       output='screen'
   )


   return LaunchDescription([
       gz_sim, 
       DeclareLaunchArgument('rviz', default_value='true', description='Open RViz.'),
       bridge, 
       rviz_node 
   ])