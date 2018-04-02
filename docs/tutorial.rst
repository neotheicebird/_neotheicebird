Tutorial
========

You can create a similar About-me package and deploy to Pypi. Here are the steps to doing that from scratch.

1. Project template

The best practises used in this project come from a great template code from U.S. Geological Survey (https://github.com/usgs)

To create the template, we are going to use cookiecutter. First install cookiecutter.

.. highlight::shell
    pip install cookiecutter

To know more about cookiecutter go to: https://github.com/audreyr/cookiecutter

You can then download the template code using the following command. You will be asked a set of questions that configures the project.

.. highlight::shell
    cookiecutter https://github.com/usgs/cookiecutter-python-package.git

You can name your project the same as your github handle. You will be answering prompts like this:

.. highlight::markdown
    full_name [Jeremiah Lant]: Clarence King
    email [jlant@usgs.gov]: cking@usgs.gov
    project_name [pyproj]: Fortieth Parallel
    project_slug [fortieth_parallel]: <Enter>
    project_short_description [pyproj contains all the files and directories you need to create a Python project.]: fortieth_parallel is a command line utility that narrates the geologic exploration of the Fortieth Parallel
    release_date [2016-05-14]: 1878-01-01
    year [1878]: <Enter>
    version [0.1.0]: <Enter>
    reviewed_and_approved [no]: yes

2. Create a virtual environment for your code. Let's assume your github handle is the project name.

.. highlight::shell
    virtualenv -p /usr/bin/python3 projectEnv
    source projectEnv/bin/activate
    cd <yourgithubhandle>

Make sure you do not add the virtualEnv to version control later.

You can edit each of the rst file to your suiting. Your core logic lies in the folder <yourgithubhandle>. You can also write tests in the tests/ directory that will be run later using pytest.

Make sure you edit the ``setup.py`` file and see to that all information in it are correct.

4. Create a github repo with project name <yourgithubhandle>

5. Locally lets initialize the repo as a git repo and add all the files to it.

.. highlight::shell
    git init
    git add .
    git commit -m "first commit"

6. Create a MANIFEST.in file. To do that you can

.. highlight::shell
    pip install check-manifest
    check-manifest -c

MANIFEST, is the exact list of files to include in your source distribution for packaging later. We are creating it now, since TOX which we will install next needs MANIFEST.in to run without giving an error.

7. Install TOX for automated testing. Lets install tox and use it.

.. highlight::shell
    pip install tox

create a tox.ini file with the following content.

.. highlight::markdown
    [tox]
    envlist = py27, py36

    [testenv]
    commands = pytest
    deps =
        pytest

This tells tox to test against python 2.7 and 3.6 using the pytest command. If the tests pass, you are good to go further.

8. Before pushing our code to Github, lets connect the Github repo to some services. Two services we are going to use are:

    a. Travis CI: A continuous integration service, that automates building and testing on a server and also follows up successful builds with deploy to production or other commands. This is useful to learn when we create apps and run big developments. Its a great practise that eradicates bugs quickly.
    b. Read the Docs: For documentation using sphinx. All the documentation that are to be rendered on readthedocs.io are generated from the /docs directory of your repo. Edit the text files to make changes.

9. Connecting to Travis CI:
    a. Go to https://Travis.io and sign in using your Github account.
    b. You can go to https://travis-ci.org/profile run sync and switch on travis for your Github project.
    c. Add a ``.travis.yml`` file to your local project repo. You would have to look into Travis's docs to find out how to configure this file.
    d. To trigger a Travis build we need to push our code to Github which we will do after setting up readthedocs

10. Connecting to ReadTheDocs.io:
    a. Similar to Travis, go to https://readthedocs.org/
    b. Sign up for an account and point things to your Github account
    c. Click on "Import Project" and import this project repo.

11. Time to see our changes

.. highlight::shell
    git remote add origin https://github.com/<yourgithubhandle>/<yourgithubhandle>
    git push origin master

This code push should trigger both Travis and ReadTheDocs builds. Your documentation would be created on https://<yourgithubhandle>.readthedocs.io

12. Before publishing our code to PyPI, we need to create a distribution. We are going to create a wheel distribution for this project.

.. highlight::shell
    python setup.py --help-commands

``setup.py`` serves as both a place for configuring your project details and also for exposing various tools we need to package and distribute our code.

Before creating a wheel distribution, create a file named ``setup.cfg`` with contents:

.. highlight::markdown
    [bdist_wheel]
    universal=1

To create the wheel distribution, run:

.. highlight::shell
    python setup.py bdist_wheel

You should see a ``dist/`` folder with a wheel file all ready for upload.

While ``setup.py`` has an upload to PyPI tool, we are not going to use it as its less secure than other options. For the upload we are going to use ``twine``

.. highlight::shell
    pip install twine

The final step is to upload the ``dist/*`` contents to PyPI. Before doing that we need to register for an account in PyPI, which can be obtained from https://pypi.org/account/register/

You can create a ``.pypirc`` file in your ``$HOME`` directory with the username and password for easier upload. Or leave this step if you wish to enter the credentials during each upload.

13. Uploading the distribution.

To upload the distribution, you can do:

.. highlight::shell
    twine upload dist/*

There is also a TestPyPI index which can be used to test this upload before uploading to the real index. You can register for TestPyPi account too. For that checkout https://packaging.python.org/guides/using-testpypi/