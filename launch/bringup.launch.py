"""Start the official TurtleBot3 Gazebo world followed by its Nav2 stack."""

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():
    gazebo_share = get_package_share_directory('turtlebot3_gazebo')
    navigation_share = get_package_share_directory('turtlebot3_navigation2')
    default_map = os.path.join(navigation_share, 'map', 'map.yaml')
    default_params = os.path.join(navigation_share, 'param', 'humble', 'burger.yaml')

    map_arg = DeclareLaunchArgument(
        'map', default_value=default_map,
        description='Map that matches the upstream turtlebot3_world Gazebo world.',
    )
    nav2_delay_arg = DeclareLaunchArgument(
        'nav2_delay', default_value='20.0',
        description='Seconds to let Gazebo initialize before starting Nav2.',
    )
    gazebo = IncludeLaunchDescription(PythonLaunchDescriptionSource(
        os.path.join(gazebo_share, 'launch', 'turtlebot3_world.launch.py')))
    nav2 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(navigation_share, 'launch', 'navigation2.launch.py')),
        launch_arguments={
            'map': LaunchConfiguration('map'),
            'params_file': default_params,
            'use_sim_time': 'true',
        }.items(),
    )

    return LaunchDescription([
        map_arg,
        nav2_delay_arg,
        gazebo,
        TimerAction(period=LaunchConfiguration('nav2_delay'), actions=[nav2]),
    ])
