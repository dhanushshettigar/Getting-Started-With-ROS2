from setuptools import find_packages, setup

package_name = 'diff_robot_custom_world'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/models/vehicle', [
            'models/vehicle/model.sdf',
            'models/vehicle/model.config'
        ]),
        ('share/' + package_name + '/worlds', ['worlds/my_world.sdf']),
        ('share/' + package_name + '/launch', ['launch/diff_drive.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='dhanush',
    maintainer_email='dhanushshettigar90@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
