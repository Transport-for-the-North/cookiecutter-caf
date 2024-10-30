# -*- coding: utf-8 -*-
"""Module containing extensions for Jinja2 for use within the template."""

##### IMPORTS #####

import re
import string

from cookiecutter.utils import simple_filter

##### CONSTANTS #####


##### CLASSES & FUNCTIONS #####

@simple_filter
def remove_prefix(name: str, prefix: str) -> str:
    """Remove given prefix from name."""
    prefix = re.escape(prefix)
    return re.sub(rf"^{prefix}", "", name.strip(), flags=re.I)

@simple_filter
def pkg_name(name: str, remove_caf: bool = False) -> str:
    """Remove characters not allowed in Python package names."""
    name = str(name).strip().lower()
    
    if remove_caf:
        name = name.removeprefix("caf.")

    name = re.sub(r"[\s_.-]+", "_", name)

    # Remove all non-allowed characters
    allowed_characters = string.ascii_letters + string.digits + "_"
    name = re.sub(rf"[^{allowed_characters}]", "", name)

    # Remove non-starting characters
    name = re.sub(rf"^[{string.digits}]+", "", name)

    name = re.sub(r"_+", "_", name)

    return name


@simple_filter
def repo_name(name: str, remove_caf: bool = False) -> str:
    """Remove characters not allowed in repository names."""

    if remove_caf:
        name = name.removeprefix("caf.")

    name = str(name).strip().lower()
    name = re.sub(r"[\s]+", "-", name)

    # GitHub restricts repo names to ASCII letters and digits and characters ., -, and _
    allowed_characters = string.ascii_letters + string.digits + r".\-_"
    name = re.sub(rf"[^{allowed_characters}]", "", name)

    name = re.sub(r"-+", "-", name)

    return name


def _test_pkg_name():
    """These only work when simple_filter decorator is commented out."""
    tests = [
        "no_change",
        "test",
        " strip   ",
        "spaces in    words",
        "hyphens-are--bad--",
        "not£%$-*&^£allowed",
        "space -_hyphen_ -underscore",
        "090starting090",
        string.punctuation,
        string.ascii_lowercase,
        string.ascii_uppercase,
        string.whitespace,
    ]

    length = max(len(i) for i in tests)
    for i in tests:
        print(f"pkg_name  {i!r:>{length}.{length}} -> {pkg_name(i)!r}")
        print(f"repo_name {i!r:>{length}.{length}} -> {repo_name(i)!r}")


if __name__ == "__main__":
    _test_pkg_name()
