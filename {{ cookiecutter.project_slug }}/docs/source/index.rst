.. {{ cookiecutter.__readable_name }} documentation master file.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive. See the
   `reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_
   documentation for details.

Welcome to {{ cookiecutter.__readable_name }}'s documentation!
===========================================================

{{ cookiecutter.description }}

{{ cookiecutter.__readable_name }} source code is available on `GitHub <{{ cookiecutter.github_url }}>`_.

{% if cookiecutter.caf %}

Common Analytical Framework
---------------------------

This package is sits within the `Common Analytical Framework (CAF) <https://transport-for-the-north.github.io/caf_homepage/intro.html>`_,
which is a collaboration between transport bodies in the UK to develop and maintain commonly use
transport analytics and appraisal tools.
{% endif %}

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   user_guide
   api
   examples/index


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
