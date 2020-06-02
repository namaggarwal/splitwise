from setuptools import setup, find_packages
from os import path

INSTALL_REQUIRES = []
INSTALL_REQUIRES.append('oauth2')

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
  long_description = f.read()


setup(name='splitwise',
      version='1.2.0',
      description='Splitwise API SDK',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='Naman Aggarwal',
      author_email='nam.aggarwal@yahoo.com',
      url='https://github.com/namaggarwal/splitwise',
      download_url='https://github.com/namaggarwal/splitwise/tarball/1.1.0',
      license='MIT License',
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
