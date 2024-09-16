# Always get the current version in "editable" installs
# `pip install -e .` / `python setup.py develop`
def _get_version() -> str:
    from pathlib import Path

    from versioningit import get_version

    return get_version(
        project_dir=Path(__file__).parents[
            {%- if cookiecutter.caf -%} 3 {%- else -%} 2 {%- endif -%}
        ],
    )


# The following _get_version() call will get replaced by versioningit with a
# static version string during a build
__version__ = _get_version()
