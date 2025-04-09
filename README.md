# Cookiecutter-CAF

Cookiecutter template for Transport for the North's packages, this template works for both
CAF and non-CAF (default) packages.

## Usage

This template is setup to work with Cookiecutter, which will automatically fill in the template
details provided by the user. See [Cookiecutter documentation](https://cookiecutter.readthedocs.io/en/stable/index.html)
for more details.

The template can be used with cookiecutter with (see [Cookiecutter Setup](#cookiecutter-setup)
for installation details):

`cookiecutter gh:Transport-for-the-North/cookiecutter-caf`

Cookiecutter will then ask the user to provide the required parameters and answer the setup
questions and will then create the repository folder locally and, if enabled, initialise git.
Git can be initialised manually from the git command-line utility or within GitHub desktop,
if preferred.

### Parameters

This template will ask for some parameters about the project, and will use these during the
generation of the project folder. The parameters contain sensible defaults (highlighted in blue
brackets) which should be used for many of the parameters, the full set of parameters are:

- **Project Name:** name of the project, this can contain any characters but it recommended to
  be very few words (ideally one).
- **CAF package?:** whether this package is a CAF package i.e. should have "caf." prepended to it.
  This defaults to not prepending "caf." to the project name.
- **Full Package Name:** the full "normalised" Python package name, this is generated based on the
  project name and in most cases the **generated default should be used**. The generation converts
  the project name to lowercase, replaces spaces with underscores and removes some characters
  which aren't allowed in Python package names.
- **Full Repository Name:** the full "normalised" git repository name, this is also generated based
  on the project name and again the **generated default should be used** in most cases. This
  generation converts the project name to lowercase, replaces spaces with hyphens and remove some
  characters which aren't allowed in repository names.
- **Author:** the author of the project, this should be Transport for the North (default) for any
  projects created for / by TfN staff.
- **GitHub Organisation Account:** the actual name of the GitHub organisation account, this is
  generated from the author which should be left as default for TfN projects. The generation is done
  by converting the author to lowercase, replacing spaces with hyphens and removing any invalid
  characters, this should be be checked against the GitHub account name the repository will be
  stored on.
- **GitHub Source Code URL:** the full URL of the GitHub repository where the project should be
  stored, this is generated from the GitHub organisation account and the repository name. This
  URL should be checked against GitHub and manually input if required.
- **Project Maintainers:** the name(s) of the project maintainers with their GitHub username in
  brackets, if providing multiple names these should be separated with semi-colons.
- **Package Description:** short description of the package, will be included in the generated
  README and the package metadata.
- **Initialise Git Repository:** if y(es) will initialise the folder as a local git repository,
  this will not create the repository on GitHub.
- **Push Repository to GitHub:** if y(es) will push (upload) the local git repository to a GitHub
  repository, an empty GitHub repository must exist at the correct URL or this will fail.

> **Note:** the [git](https://git-scm.com/) command-line utility is required for the
> repository initialisation and push to GitHub processes.

## Template Details

This section provides some more details on what is produced by the template generation,
including providing details on some of the specific sub-folders which are created.

### What does this template provide?

This template sets up a lot of CI/CD (Continuous Integration / Continuous Deployment) tools
to help manage, update, release, and test a new python package. Here is a list of what
this sets up for you:

- Automatic and easy to use code linting / analysis which works on your machine, which provides:
  - MyPy type checking
  - Pylint syntax checking
  - PyDocStyle documentation checking
  - Test running via pytest
- Setup for [Black](https://github.com/psf/black) code formatter
  - This can be run with `black src` or `black tests` from the root of this repo
- GitHub actions which run on all pull requests and pushes to main
  - These run the above tox and black checks and will warn you where code deviates from the standards
- Automatic code versioning via Git Tags
- Lays out the package in a consistent format to fit the Python package structure.

### docs

All documentation for the package should go in here, this template provides the basic structure
for Sphinx documentation and automatically includes API documentation so `sphinx-quickstart` does
not need running. For more details on using Sphinx see the
[Sphinx Getting Started documentation](https://www.sphinx-doc.org/en/master/usage/quickstart.html).

This template sets up a basic structure with pages for a user guide and automatic API documentation
ready for use. Sphinx documentation is made up of plaintext documents written in
reStructuredText (reST) markup language, with the starting page define in `index.rst` all other
pages can be linked to from the main table of contents. The Sphinx documentation contains a detailed
[reStructuredText Primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)
which explains how to write rst files.

The documentation is all stored within the `docs/source` folder and can be generated using the make
batch file with `make html` for web-based documentation. A separate documentation requirements file
(`docs/requirements.txt`) is provided to list any additional requirements required e.g. sphinx itself.

### Package folder

The `{{ cookiecutter.__pkg_folder }}` folder will be updated with the package name when running
cookiecutter. All code goes in here. Some files already exist:

- `__init__.py` - this is the entry point for your package and should contain a docstring
  describing the package and alias imports to the key functions / classes the package provides.
- `_version.py` - this is the version file which contains package version information and is
  managed automatically by versioningit.
- `py.typed` - this tells python and PyPI that your package is typed, and it should
  look for type hints in the code.

### tests

All tests go here.
Tests should be written in pytest and should follow the same structure as the src package
(minus the src/caf/{package_name}). See the [pytest](https://docs.pytest.org/en/7.2.x/)
documentation for full detail, or [caf.toolkit](https://github.com/Transport-for-the-North/caf.toolkit)
for an example.

### files

There's a few files stored in the root of the package which are standard setup files. They are
listed and detail below:

- `pyproject.toml` - A file of settings and metadata for the package. This file details how to
  build the package and defines common linter tool setup.
- `RELEASE.md` - A standard file explaining the versions system.
- `requirements.txt` - Details the packages and their versions that this package depends on. It's a
  list of the python packages which must be installed for this package to work. Update this file
  as your package gains dependencies.
- `requirements_dev.txt` - Details the packages and their versions that this package depends on during
  testing and linting. These are extra dependencies on top of the `requirements.txt` ones. This is
  used by package tools to ensure your tests pass when you say they should! This file likely doesn't
  need changing very often.

### VersioningIt

[VersioningIt](https://github.com/jwodder/versioningit)
is an automatic versioning tool for GitHub based projects. It provides
consistent and predictable naming based on the number of commits since the last
user defined version. This way it can be used to find old versions of code, even
if it's just a random commit in your repo!
The version strings are user configurable, but currently configured to generate
a unique version string for every commit. See the `versioningit` section at the
bottom of `pyproject.toml` for full details.

Thanks to all the files in this repo, VersioningIt is fully set up and ready
to use! It will work with deployed packages, and those using editable installs.
Editable installs are useful for local testing during development, and can be
done by running the following in the root of a package:

`pip install -e .`

VersioningIt is based off of git Tags, which you can set on GitHub. Version
tags should start with a 'v' and contain three numbers (following the
[Semantic Versioning](https://semver.org/) convention) e.g., `v0.1.0` for an
initial version that isn't ready for a full `v1.0.0` release.

---

## Cookiecutter Setup

Cookiecutter is a Python package provided with a command-line utility, the recommended way to
install this is using [pipx](https://pipx.pypa.io/stable/).

To install pipx you will need a version of Python installed on your machine (and accessible
within the command-prompt), pipx can be installed with `pip install pipx`. Once pipx is installed
use `pipx ensurepath` to add pipx's executable folder to the PATH variable so anything installed
is accessible.

Installing cookiecutter with pipx is: `pipx install cookiecutter`. This will install and setup
the command-line utility so it can be called using the `cookiecutter` command.

## Cookiecutter Structure

This section gives a brief outline of the structure of the cookiecutter template itself,
for more information on creating / editing cookiecutter templates see
[Cookiecutter Additional Tutorials](https://cookiecutter.readthedocs.io/en/2.0.2/tutorials.html).

### cookiecutter.json

The cookiecutter.json file contains the variables and parameters used within the template.

### hooks

The hooks directory contains any Python scripts which are ran during the template generation.

### `{{ cookiecutter.project_slug }}`

The `{{ cookiecutter.project_slug }}` directory contains all the files which make up the template
these are the files / folders which will be created in the output. The jinja2 templating engine
will be automatically applied to these files to infill anywhere where there are `{{ }}` or `{% %}`.
See [Jinja Template Documentation](https://jinja.palletsprojects.com/en/3.1.x/templates/#) for
more details.
