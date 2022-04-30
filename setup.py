import versioneer
from setuptools import setup, find_packages

setup(
    name='live-subtitling-webapp',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='/',
    author='live-subtitling-webapp',
    packages=find_packages(),
    include_package_data=True,
    license='Live subtitling webapp'
)
