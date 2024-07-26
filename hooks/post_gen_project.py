# -*- coding: utf-8 -*-
"""Post cookiecutter project generation hook."""

##### IMPORTS #####
import pathlib
import subprocess

##### CONSTANTS #####

CAF = "{{ cookiecutter.caf }}".strip().lower()
INIT_GIT = "{{ cookiecutter.init_git}}".strip().lower()


##### CLASSES & FUNCTIONS #####


def _underline_print(msg: str) -> None:
    print("", msg, "-" * len(msg), sep="\n")


def caf_setup():
    """Create parent CAF folder for package"""
    _underline_print("Creating CAF directory")
    caf_dir = pathlib.Path("src/caf")
    caf_dir.mkdir()

    project_dir = pathlib.Path("src/{{ cookiecutter.__pkg_name }}")
    project_dir.rename(caf_dir / project_dir.name)
    print("Done CAF setup")


def init_git():
    """Initialise git repository and push to GitHub."""
    _underline_print("Initialising git repository")
    subprocess.run(["git", "init", "-b", "main"], check=True)

    _underline_print("Creating initial commit")
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(
        ["git", "commit", "-m", "Initial commit from cookiecutter template"], check=True
    )

    _underline_print("Adding remote {{ cookiecutter.github_url }}")
    subprocess.run(
        ["git", "remote", "add", "origin", "{{ cookiecutter.github_url }}"], check=True
    )

    _underline_print("Pushing to GitHub")
    subprocess.run(["git", "push", "--set-upstream", "main"], check=True)

    _underline_print("Completed git setup")


def main():
    """Setup CAF directory and commit to git, if enabled."""
    if CAF == "true":
        caf_setup()

    if INIT_GIT == "true":
        try:
            init_git()
        except Exception as exc:
            raise SystemExit(
                f"\n{'-' * 22} ERROR {'-' * 22}\n"
                f"Error initialising git repository: {exc}\n"
                "Try setting init_git to False to use the template"
                f" without setting up the git repository.\n{'-' * 51}\n"
            ) from exc


if __name__ == "__main__":
    main()
