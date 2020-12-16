from setuptools import setup, find_packages
import sys
import platform

# python version check
python_min_version = (3, 6, 2)
python_min_version_str = '.'.join(map(str, python_min_version))
if sys.version_info < python_min_version:
    print(
        f"You are using Python {platform.python_version()}. At least Python >={python_min_version_str} is required.")
    sys.exit(-1)


setup(
    name='gooogloo',
    version='0.0.1',
    author='sansmoraxz',
    # fix this to use `find_packages`
    packages=['gooogloo', 'gooogloo.modules', 'gooogloo.modules.utils'],
    url='https://github.com/sansmoraxz/py-gooogloo',
    license='LICENSE',
    description='Easy google search for python'
)
