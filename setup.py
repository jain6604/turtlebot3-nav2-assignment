from glob import glob
from setuptools import setup

package_name = 'turtlebot3_nav2_assignment'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', glob('launch/*.launch.py')),
        ('share/' + package_name + '/models/demo_obstacle', glob('models/demo_obstacle/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Saksham Jain',
    maintainer_email='sj6261083960@gmail.com',
    description='Assignment launch and repeatable obstacle test for TurtleBot3 Nav2.',
    license='MIT',
    entry_points={'console_scripts': [
        'spawn_obstacle = turtlebot3_nav2_assignment.spawn_obstacle:main',
    ]},
)
