from setuptools import find_packages, setup

package_name = 'sosin_control'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    package_data={'': ['py.typed']},
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Fırat Serhatlı',
    maintainer_email='frtsrhtli@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'konum_oku = sosin_control.konum_oku:main',
            'acik_dongu_kare = sosin_control.acik_dongu_kare:main',
            'ileri_git = sosin_control.ileri_git:main',
            'merhaba = sosin_control.merhaba:main',
        ],
    },
)
