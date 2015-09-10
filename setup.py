from setuptools import setup, find_packages

setup(
    name = "beets-frompath",
    version = "0.0.1",
    description="beets plugin to use the file path to update the album/title info",
    long_description=open('README.rst').read(),
    author='blxd',
    url='https://github.com/blxd/beets-frompath',
    download_url='https://github.com/blxd/beets-frompath.git',
    license='MIT',

    packages=['beetsplug'],
    namespace_packages=['beetsplug'],
    install_requires = ['beets>=1.3.7']
)