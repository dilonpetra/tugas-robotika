from setuptools import setup
import os
from glob import glob

package_name = 'convert_teleop_ros1_to_ros2'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='dilonpetra',
    maintainer_email='dilonpetra@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'convert_teleop_ros1_to_ros2 = convert_teleop_ros1_to_ros2.convert_teleop_ros1_to_ros2:main'
        ],
    },
)
