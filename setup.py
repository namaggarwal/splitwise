from setuptools import setup, find_packages
import os

INSTALL_REQUIRES = []
INSTALL_REQUIRES.append('oauth2')

license='MIT'
if os.path.exists('LICENSE'):
  license = open('LICENSE').read()

long_description = """
    The Splitwise SDK provides Splitwise APIs to get data from your Splitwise Account.
    1. https://github.com/namaggarwal/splitwise - README
    2. https://github.com/namaggarwal/flask-splitwise-example - Sample
  """

setup(name='splitwise',
      version='1.0.0',
      description='Splitwise API SDK',
      long_description=long_description,
      author='Naman Aggarwal',
      author_email='nam.aggarwal@yahoo.com',
      url='https://github.com/namaggarwal/splitwise',
      download_url='https://github.com/namaggarwal/splitwise/tarball/1.0.0',
      license=license,
      packages=find_packages(),
      classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules'
        ],
        install_requires=INSTALL_REQUIRES
)
