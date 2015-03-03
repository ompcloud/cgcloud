from setuptools import setup, find_packages

dependency_base_url = 'git+https://github.com/BD2KGenomics/'

setup(
    name="cgcloud-core",
    version="1.0.dev1",
    package_dir={ '': 'src/main' },
    packages=find_packages( 'src/main' ),
    entry_points={
        'console_scripts': [
            'cgcloud = cgcloud.core.ui:main' ], },
    install_requires=[
        'bd2k-python-lib>=1.5.dev1',
        'cgcloud-lib>=1.0.dev1',
        'boto>=2.16.0',
        'Fabric>=1.7.0',
        'PyYAML>=3.10' ],
    namespace_packages=[ 'cgcloud' ],
    dependency_links=[
        dependency_base_url + 'bd2k-python-lib.git@master#egg=bd2k-python-lib-1.5.dev1',
        dependency_base_url + 'cgcloud-lib.git@master#egg=cgcloud-lib-1.0.dev1' ] )
