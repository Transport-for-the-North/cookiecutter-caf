Quick Start
===========

.. todo::
    Write brief description about the possible ways for using the tool e.g. CLI, GUI and
    importing in Python.

*{{ cookiecutter.__readable_name }} is provided as a Python package and a command-line utility.
The command-line utility aims to make some of the commonly used functionality 
available without needing to use Python code, see :ref:`usage` for details.*

{{ cookiecutter.__readable_name }} can be installed from pip, conda-forge or **pipx
(when using as a command-line utility).**

Pip
---
Installing through pip is easy and can be done in one command:
``pip install {{ cookiecutter.package_name }}``

conda-forge
-----------
Installing through conda-forge is easy and can be done in one command:
``conda install {{ cookiecutter.package_name }} -c conda-forge``

Pipx
----

.. todo::
    Does {{ cookiecutter.__readable_name }} support being installed with
    `Pipx <https://pipx.pypa.io/stable/>`__?

`Pipx <https://pipx.pypa.io/stable/>`__ is the recommended way to use {{ cookiecutter.package_name }} as a utility.
It handles installing the tool in its own container, and makes it easy to access from a terminal.

First install pipx into your default Python environment using pip or conda, see
`Pipx's installation instructions <https://pipx.pypa.io/latest/how-to/install-pipx.html>`__ for more details.

Once pipx is installed and setup caf.toolkit can be installed using ``pipx install {{ cookiecutter.package_name }}``,
this should make it available in command-line anywhere using ``{{ cookiecutter.package_name }} ...``.

.. seealso::
    `Pipx Getting started <https://pipx.pypa.io/latest/tutorial/getting-started.html>`__ for
    more information about using pipx.

Usage
-----

.. todo::
    Does {{ cookiecutter.__readable_name }} have a CLI or GUI?

More details can be found in :ref:`tool usage`.

Python
^^^^^^

.. todo::
    Does {{ cookiecutter.__readable_name }} have a suggested alias?

When using {{ cookiecutter.__readable_name }} functionality within Python:

.. code:: python

    import {{ cookiecutter.package_name }}

The :ref:`user guide` contains :ref:`tutorials` and :ref:`code examples`, which
explain available functionality. For a detailed look at the
package API see :ref:`API Reference`.
