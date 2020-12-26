import setuptools as setuptools
import re
from os.path import join




with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name="Supycap",
  version= '2.4',
  author="Yuan Chen",
  author_email="yuan.chen18@imperial.ac.uk",
  description="A python library for GCD analysis of supercapacitors",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/",
  packages=setuptools.find_packages(),
  install_requires=(
      'scipy', 
      'matplotlib', 
      'numpy',
      'pandas',
      'IPython', 
      'sklearn',
      'datetime',
  ),
  include_package_data = True,
  platforms = 'any',
  classifiers=[
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: MIT License",
  "Operating System :: OS Independent",
  ],
)