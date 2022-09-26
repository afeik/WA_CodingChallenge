from setuptools import setup

package_name = 'merge_arrays'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='andi',
    maintainer_email='feik.andi@gmail.com',
    description='merge two array',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'merge_arrays_node = merge_arrays.mergearray:main',
            'array1_publish = merge_arrays.array1_publish:main',
            'array2_publish = merge_arrays.array2_publish:main',

        ],
    },
)
