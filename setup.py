#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("CHANGELOG.rst") as changelog_file:
    changelog = changelog_file.read()

with open("LICENSE") as license_file:
    license = license_file.read()


requirements = []

test_requirements = [
    "pytest",
]


setup(
    name="neotheicebird",
    version="0.1.1",
    description="Its a package that describes me. Kinda like an about-me page. You can learn about me by installing the library and importing it.",
    long_description=readme + "\n\n" + changelog,
    author="Prashanth Gandhiraj",
    author_email="neotheicebird@gmail.com",
    url="",
    project_urls={
        "Source Code": "https://github.com/neotheicebird/neotheicebird"
    },
    packages=[
        "neotheicebird",
    ],
    package_dir={"neotheicebird":
                 "neotheicebird"},
    include_package_data=True,
    install_requires=requirements,
    license=license,
    zip_safe=False,
    keywords="neotheicebird about aboutme about-me learn packaging for pypi",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",
        "Natural Language :: English",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
    test_suite="tests",
    tests_require=test_requirements
)
