import os
import codecs
from setuptools import (setup, find_packages)


with codecs.open(os.path.normpath(path=os.path.join(os.path.abspath(path=os.path.dirname(p=__file__)) , r"README.md")) , encoding="utf-8") as fh:
    long_description = "\n" + fh.read()


setup(
    name="github4api",
    version='1.1.5',
    author="Shervin Badanara (shervinbdndev)",
    maintainer="Shervin Badanara",
    author_email="shervin2234@gmail.com",
    description='A python Package API for getting Github Users Information.',
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages() ,
    project_urls={
        'Source':'https://www.github.com/shervinbdndev/github4api/'
    },
    license='MIT',
    install_requires=['bs4', 'colorama', 'html5lib', 'requests', 'poetry'] ,
    keywords=['python', 'api', 'github', 'github_api', 'github_package'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ] ,
    extras_require={
        'dev':['check-manifest'] ,
        'test' : ['coverage'] ,
    }
)