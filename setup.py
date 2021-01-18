import sys
from setuptools import setup, find_packages
from geolang import __version__, __author__

assert sys.version >= "3.6", "Requires Python v3.6 or above versions."

try:
    desc = open('README.rst').read()
except FileNotFoundError:
    desc = 'see README.rst'

setup(
    name="geolang",
    version=__version__,
    description="Simple Georgian Language ToolKit",
    long_description=desc,
    author=__author__,
    author_email="Lh4cKg@gmail.com",
    url="https://github.com/Lh4cKg/simple-geolang-toolkit/",
    download_url="https://github.com/Lh4cKg/simple-geolang-toolkit/tarball/v0.2.0",
    packages=find_packages(),  # ["geolang"],
    license="MIT",
    keywords=['geolang', 'Simple', 'Georgian', 'Language', 'ToolKit'],
    classifiers=[
        "Environment :: Console",
        "Environment :: Web Environment",
        "License :: OSI Approved :: Python Software Foundation License",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
