import os
from setuptools import setup
from pystatsd import VERSION

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "pystatsd",
    version=".".join(map(str, VERSION)),
    author = "Steve Ivy",
    author_email = "steveivy@gmail.com",
    description = ("pystatsd is a client for Etsy's statsd server, a front end/proxy for the Graphite stats collection and graphing server."),
    url='https://github.com/sivy/py-statsd',
    license = "BSD",
    install_requires=['zbxsend'],
    packages=['pystatsd'],
    long_description=read('README.md'),
    classifiers=[
        "License :: OSI Approved :: BSD License",
    ],
    scripts=['bin/pystatsd-server']
)
