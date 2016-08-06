from setuptools import setup, find_packages

INSTALL_REQUIRES = []
INSTALL_REQUIRES.append('oauth2')

setup(name='splitwise',
      version='0.0.1',
      description='Splitwise API SDK',
      long_description='SDK to use Splitwise APIs',
      author='Naman Aggarwal',
      author_email='nam.aggarwal@yahoo.com',
      url='http://namaggarwal.github.io/',
      license='MIT',
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
