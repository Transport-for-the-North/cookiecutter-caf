![Transport for the North Logo]({{ cookiecutter.github_url }}/blob/main/docs/TFN_Landscape_Colour_CMYK.png)

<h1 align="center">{{ cookiecutter.project_slug }}</h1>

<p align="center">
<a href="https://www.gnu.org/licenses/gpl-3.0.en.html">
  <img alt="License: GNU GPL v3.0" src="https://img.shields.io/badge/license-GPLv3-blueviolet.svg?style=flat-square">
</a>
<a href="https://github.com/psf/black">
  <img alt="code style: black" src="https://img.shields.io/badge/code%20format-black-000000.svg">
</a>
<a href='https://{{ cookiecutter.project_slug.replace(".", "") }}.readthedocs.io/en/stable/?badge=stable'>
  <img alt='Documentation Status' src="https://img.shields.io/readthedocs/{{ cookiecutter.project_slug.replace('.', '') }}?style=flat-square&logo=readthedocs">
</a>
<a href="https://pypi.org/project/{{ cookiecutter.project_slug }}/">
  <img alt="Supported Python versions" src="https://img.shields.io/pypi/pyversions/{{ cookiecutter.project_slug }}.svg?style=flat-square">
</a>
</p>

<p align="center">
<a href="https://pypi.org/project/{{ cookiecutter.project_slug }}/">
  <img alt="Latest release" src="https://img.shields.io/github/release/{{ cookiecutter.github_org }}/{{ cookiecutter.project_slug }}.svg?style=flat-square&maxAge=86400">
</a>
<a href="https://anaconda.org/conda-forge/{{ cookiecutter.project_slug }}">
  <img alt="Conda" src="https://img.shields.io/conda/v/conda-forge/{{ cookiecutter.project_slug }}?style=flat-square&logo=condaforge">
</a>
<a href="{{ cookiecutter.github_url }}/actions?query=event%3Apush">
  <img alt="Testing Badge" src="https://img.shields.io/github/actions/workflow/status/{{ cookiecutter.github_org }}/{{ cookiecutter.project_slug }}/tests.yml?style=flat-square&logo=GitHub&label=Tests">
</a>
<a href="https://app.codecov.io/gh/{{ cookiecutter.github_org }}/{{ cookiecutter.project_slug }}">
  <img alt="Coverage" src="https://img.shields.io/codecov/c/github/{{ cookiecutter.github_org }}/{{ cookiecutter.project_slug }}.svg?branch=master&style=flat-square&logo=CodeCov">
</a>
</p>

{{ cookiecutter.description }}

{% if cookiecutter.__pkg_name == "{package_name}" %}
Template usage and information is shown in [Template Usage](#template-usage) section below.
{% endif %}

{% if cookiecutter.caf %}

## Common Analytical Framework

This package is sits within the [Common Analytical Framework (CAF)](https://transport-for-the-north.github.io/caf_homepage/intro.html),
which is a collaboration between transport bodies in the UK to develop and maintain commonly use
transport analytics and appraisal tools.
{% endif %}

## Contributing

{{ cookiecutter.project_slug }} happily accepts contributions.

The best way to contribute to this project is to go to the [issues tab]({{ cookiecutter.github_url}}/issues)
and report bugs or submit a feature request. This helps {{ cookiecutter.project_slug }} become more
stable and full-featured. Please check the closed bugs before submitting a bug report to see if your
question has already been answered.

Please see [CONTRIBUTING.rst](contributing.rst) for details on contributing to the codebase or
documentation.

## Documentation

Documentation is created using [Sphinx](https://www.sphinx-doc.org/en/master/index.html) and is hosted online at
[{{ cookiecutter.project_slug.replace(".", "") }}.readthedocs](https://{{ cookiecutter.project_slug.replace(".", "") }}.readthedocs.io/en/stable/).
The documentation can be built locally using the provided make batch files, inside the docs folder,
with `make html`.

{% if cookiecutter.__pkg_name == "{package_name}" %}
---

## Template Usage

Find all occurrences of "{{ cookiecutter.__pkg_name }}" and replace it with the package name.
Then remove this section explaining how to use the template and write a description of the
package above.

{{ cookiecutter._template_details }}

---
{% endif %}
