Quick Start
===========

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

.. attention::
    Does {{ cookiecutter.__readable_name }} support being installed with
    `Pipx <https://pipx.pypa.io/stable/>`__?


Usage
-----

.. attention::
    Does {{ cookiecutter.__readable_name }} have a CLI or GUI?

More details can be found in :ref:`tool usage`.

Python
^^^^^^

.. attention::
    Does {{ cookiecutter.__readable_name }} have a suggested alias?

When using {{ cookiecutter.__readable_name }} functionality within Python:

.. code:: python

    import {{ cookiecutter.package_name }}

The :ref:`user guide` contains :ref:`tutorials` and :ref:`code examples`, which
explain available functionality. For a detailed look at the
package API see :ref:`API Reference`.
