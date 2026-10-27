"""Spawn an SDF obstacle through Gazebo's /spawn_entity service."""

import argparse
from pathlib import Path
import rclpy
from rclpy.node import Node
from gazebo_msgs.srv import SpawnEntity


class ObstacleSpawner(Node):
    def __init__(self):
        super().__init__('assignment_obstacle_spawner')
        self.client = self.create_client(SpawnEntity, '/spawn_entity')

    def spawn(self, name, x, y):
        if not self.client.wait_for_service(timeout_sec=15.0):
            raise RuntimeError('/spawn_entity service unavailable; start Gazebo first.')
        sdf_path = Path(__file__).resolve().parents[1] / 'models' / 'demo_obstacle' / 'model.sdf'
        request = SpawnEntity.Request()
        request.name = name
        request.xml = sdf_path.read_text(encoding='utf-8')
        request.robot_namespace = ''
        request.reference_frame = 'world'
        request.initial_pose.position.x = x
        request.initial_pose.position.y = y
        future = self.client.call_async(request)
        rclpy.spin_until_future_complete(self, future, timeout_sec=20.0)
        if future.result() is None:
            raise RuntimeError('Timed out spawning obstacle.')
        if not future.result().success:
            raise RuntimeError(future.result().status_message)
        self.get_logger().info(f'Spawned {name} at ({x:.2f}, {y:.2f}).')


def main():
    parser = argparse.ArgumentParser(description='Spawn a laser-visible Nav2 test obstacle.')
    parser.add_argument('--name', default='demo_obstacle')
    parser.add_argument('--x', type=float, required=True)
    parser.add_argument('--y', type=float, required=True)
    args = parser.parse_args()
    rclpy.init()
    node = ObstacleSpawner()
    try:
        node.spawn(args.name, args.x, args.y)
    finally:
        node.destroy_node()
        rclpy.shutdown()
