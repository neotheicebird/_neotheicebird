neotheicebird
===============================

Its an "About me" page on Pip index.

This "About me" python package contains information about me as a developer.

Why did I create this package?

This package has 2 purposes:

1. Developers can simply install and import this package right from the console to know about me or my works. You can think of this package like a twitter handle and reaching to the tweets under the handle.

2. I started this project to learn more about python packaging and deployment. You can the best practises to create and deploy python packages to the PyPi index, with minimal code.

This is just like creating a Github account, or a Twitter account. Commandline is the canvas, let's express through it. Run a "commandline blog", create jokes, its all possible through a package.


Tests
-----

You can use `tox` to run automated tests for Py27 and Py36 environments.

Tutorial
--------


Setting up travis CI
--------------------

Travis CI is a continuous Integration service. Your code is built, test and even deployed (optionally) on Travis.

To setup Travis CI, you need to create an account on https://travis-ci.org using Github Sign-In. To start CI:

1. Go to [https://travis-ci.org/profile](https://travis-ci.org/profile) and Switch on this project for CI.
2. Add a `.travis.yml` file to your local project repo. The contents of this file could be:

```
language: python
python:
  - "2.6"
  - "2.7"
  - "3.3"
  - "3.4"
  - "3.5"
  - "3.5-dev"  # 3.5 development branch
  - "3.6"
  - "3.6-dev"  # 3.6 development branch
  - "3.7-dev"  # 3.7 development branch
# command to install dependencies
install:
  - pip install -r requirements.txt
# command to run tests
script:
  - pytest # or py.test for Python versions 3.5 and below
```
3. Commit and Git push to trigger Travis to do its job.

References
----------

.. raw:: html
    <iframe width="560" height="315" src="https://www.youtube.com/embed/qOH-h-EKKac" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>