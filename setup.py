#!/usr/bin/env python

import sys
from distutils.core import setup
from setuptools import setup, find_packages
from geolang import __version__, __author__
assert sys.version >= "3.0", "Requires Python v3.0 or above versions."

try:
    desc = open('README.rst').read()
except:
    desc = 'see README.rst'

setup (
	name = "geolang",
	version = __version__,
	description = "Simple Georgian Language ToolKit",
	long_description = desc, 
	author = __author__,
	author_email = "Lh4cKg@gmail.com",
	url = "https://github.com/Lh4cKg/simple-geolang-toolkit/",
	download_url = "https://github.com/Lh4cKg/simple-geolang-toolkit/tarball/v0.1.4",
	packages = find_packages(), #["geolang"],
	license = "MIT",
	keywords = ['geolang', 'ToolKit', 'toolkit','language'],
	classifiers=[
		"Environment :: Console",
		"Environment :: Web Environment",
		"License :: OSI Approved :: Python Software Foundation License",
		"Operating System :: POSIX :: Linux",
		"Operating System :: MacOS :: MacOS X",
		"Operating System :: Microsoft :: Windows",
		"Programming Language :: Python",
		"Programming Language :: Python :: 3.0",
		"Programming Language :: Python :: 3.1",
		"Programming Language :: Python :: 3.2",
		"Programming Language :: Python :: 3.3",
		"Programming Language :: Python :: 3.4",
		"Programming Language :: Python :: 3.5",
		"Topic :: Software Development :: Libraries :: Python Modules",
          ],
)