<div align="center" style="background-color: white;">
<a href="https://www.transportforthenorth.com/">
<img src="https://www.transportforthenorth.com/wp-content/themes/tfn-theme/img/logo.svg"
  alt="Transport for the North logo">
</a>
</div>

<h1 align="center">{{ cookiecutter.__readable_name }}</h1>

<p align="center">
<a href="https://transport-for-the-north.github.io/CAF-Handbook/python_tools/framework.html">
  <img alt="CAF Status - Pre-Alpha" src="https://img.shields.io/badge/CAF%20Status-Pre--Alpha-orange">
</a>
</p>
<p align="center">
<a href="https://pypi.org/project/{{ cookiecutter.project_slug }}/">
  <img alt="Supported Python versions" src="https://img.shields.io/pypi/pyversions/{{ cookiecutter.project_slug }}.svg?style=flat-square">
</a>
<a href="https://pypi.org/project/{{ cookiecutter.project_slug }}/">
  <img alt="Latest release" src="https://img.shields.io/github/release/{{ cookiecutter.github_org }}/{{ cookiecutter.project_slug }}.svg?style=flat-square&maxAge=86400">
</a>
<a href="https://anaconda.org/conda-forge/{{ cookiecutter.project_slug }}">
  <img alt="Conda" src="https://img.shields.io/conda/v/conda-forge/{{ cookiecutter.project_slug }}?style=flat-square&logo=condaforge">
</a>
</p>
<p align="center">
<a href="{{ cookiecutter.github_url }}/actions?query=event%3Apush">
  <img alt="Testing Badge" src="https://img.shields.io/github/actions/workflow/status/{{ cookiecutter.github_org }}/{{ cookiecutter.project_slug }}/tests.yml?style=flat-square&logo=GitHub&label=Tests">
</a>
<a href="https://app.codecov.io/gh/{{ cookiecutter.github_org }}/{{ cookiecutter.project_slug }}">
  <img alt="Coverage" src="https://img.shields.io/codecov/c/github/{{ cookiecutter.github_org }}/{{ cookiecutter.project_slug }}.svg?branch=main&style=flat-square&logo=CodeCov">
</a>
<a href='{{ cookiecutter.__readthedocs_url }}/stable/'>
  <img alt='Documentation Status' src="https://img.shields.io/readthedocs/{{ cookiecutter.__docs_name }}?style=flat-square&logo=readthedocs">
</a>
</p>

> [!WARNING]  
> This package is in an early stage of development so features may change or be removed.
> If using this package it is recommended to set a specific version and check before
> upgrading to a new version.

{{ cookiecutter.description }}

> [!TIP]
> For more detailed information including a user guide, tutorials and API reference see the full
> [{{ cookiecutter.project_slug }} documentation]({{ cookiecutter.__readthedocs_url }}/stable/)

{% if cookiecutter.package_name == "package_name" %}
> [!NOTE]
> Template usage and information is shown in [Template Usage](#template-usage) section below.
{% endif %}

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Overview](#overview)
  - [What does it do?](#what-does-it-do)
  - [Main Features](#main-features)
    - [Work-in-Progress](#work-in-progress)
  - [Who is it for?](#who-is-it-for)
- [Where to get it](#where-to-get-it)
  - [Installation from GitHub](#installation-from-github)
- [Usage](#usage)
  - [Command Line](#command-line)
- [Documentation](#documentation)
- [What is CAF?](#what-is-caf)
- [Contribution](#contribution)
- [Contact Us](#contact-us)
- [Template Usage](#template-usage)

## Overview

### What does it do?

> [!ATTENTION]
> This section of the README hasn't been written yet, but it will contain a brief
> description of what the tool is intended to do.

### Main Features

> [!ATTENTION]
> This section of the README hasn't been written yet.

- **Feature 1** - description

#### Work-in-Progress

- **Work in progress feature** - description of feature not yet release.

> [!WARNING]
> These features are work-in-progress and are not available in a released version of caf.space, to
> access these features a specific branch of caf.space should be installed, see [Installation from GitHub](#installation-from-github).

### Who is it for?

- **Target audience:** *TODO*
{% if cookiecutter.caf %}
- **CAF Analytical Stage:** *TODO*

![CAF Analytical Process Diagram](https://github.com/Transport-for-the-North/.github/blob/21a428e81880639839e221940881572cdee24d5a/profile/ProcessDiagram.png?raw=true)

For more details on CAF Analytical Stages see the [description within TfN's GitHub homepage](https://github.com/Transport-for-the-North)
{% endif %}

## Where to get it

> [!ATTENTION]
> {{ cookiecutter.project_slug }} has not been published yet so cannot be installed from
> conda-forge or PyPI, see [Installation from GitHub](#installation-from-github).

The latest released version are available at the [Python
Package Index (PyPI)](https://pypi.org/project/{{ cookiecutter.project_slug }}) and on [Conda](https://anaconda.org/conda-forge/{{ cookiecutter.project_slug }}).

```sh
conda install -c conda-forge {{ cookiecutter.project_slug }}
```

```sh
pip install {{ cookiecutter.project_slug }}
```

> [!TIP]
>
> - See the [Quick Start Guide]({{ cookiecutter.__readthedocs_url }}/stable/start.html#quick-start) for more detailed instructions.
> - See the [requirements.txt](requirements.txt) for the full list of package dependencies.

### Installation from GitHub

> [!WARNING]
> Unreleased GitHub versions should **not** be considered stable.

The latest, unreleased, version can be installed directly from GitHub using:

```sh
pip install "git+{{ cookiecutter.github_url }}"
```

> [!TIP]
> `pip install` can install a specific tag, or branch, using `@{tag-name}`
> after the git URL.

## Usage

CAF.space provides and Command-line (CLI) and graphical interface (GUI) to use many of it's
features without the need to write any Python code, see the [Tool Usage section]({{ cookiecutter.__readthedocs_url }}/stable/usage/index.html)
of the user guide for more details.

### Command Line

The tool can be run from command line, with the command:

```sh
{{ cookiecutter.project_slug }}
```

See [Command-Line Interface (User Guide)]({{ cookiecutter.__readthedocs_url }}/stable/usage/cli.html)
for full explanations of the parameters.

## Documentation

The code documentation is hosted at <{{ cookiecutter.__readthedocs_url }}/stable/>.

{% if cookiecutter.caf %}

## What is CAF?

This tool is part of TfN's [Common Analytical Framework (CAF)](https://github.com/Transport-for-the-North).
CAF is Transport for the North's structured suite of analytical tools designed to support transport
modelling, appraisal, and strategic decision-making.

More information on CAF and details on other CAF tools can be found on [TfN's GitHub Homepage](https://github.com/Transport-for-the-North).
{% endif %}

## Contribution

We encourage use of, and contributions to, the repositories within this organisation, licenses are provided within
the repositories and the [organisation contribution guide](https://github.com/Transport-for-the-North/.github/blob/main/CONTRIBUTING.rst)
provides details for contributions.

---

## Contact Us

For further information about using this tool or CAF tools in your projects and work contact Transport for the North - <TfNOffer@transportforthenorth.com>

---

{% if cookiecutter.package_name == "package_name" %}

## Template Usage

Find all occurrences of "{{ cookiecutter.package_name }}" and replace it with the package name.
Then remove this section explaining how to use the template and write a description of the
package above.

{{ cookiecutter._template_details }}

---
{% endif %}

[Go to Top](#table-of-contents)
