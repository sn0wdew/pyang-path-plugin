import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="pyang-path-plugin",
    version="0.1.0",
    description=("pyang Path plugin"),
    long_description=read('README.md'),
    packages=['plugins'],
    url="https://https://github.com/sn0wdew/pyang-path-plugin",
    author="Michael Snider",
    author_email="massnider@gmail.com",
    license="BSD-2",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Telecommunications Industry",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Code Generators",
        "License :: OSI Approved :: BSD-2",
        "Programming Language :: Python",
    ],
    install_requires=[
        'pyang>=2.0.1',
        'redisearch>=0.7.0',
    ],
    include_package_data=True,
    keywords=["yang", "pyang"],
    entry_points={
        'pyang.plugin': [
            'path_pyang_plugin=plugins.sensor:pyang_plugin_init',
        ]
    }
)
