# -*- coding: utf-8 -*-
"""Post cookiecutter project generation hook."""

##### IMPORTS #####
import pathlib
import subprocess

##### CONSTANTS #####

CAF = "{{ cookiecutter.caf }}".strip().lower()
INIT_GIT = "{{ cookiecutter.init_git }}".strip().lower()
PUSH_REPO = "{{ cookiecutter.push_repository }}".strip().lower()


##### CLASSES & FUNCTIONS #####


def _underline_print(msg: str) -> None:
    print("", msg, "-" * len(msg), sep="\n")


def caf_setup():
    """Create parent CAF folder for package"""
    _underline_print("Creating CAF directory")
    caf_dir = pathlib.Path("src/caf")
    caf_dir.mkdir()

    project_dir = pathlib.Path("src/{{ cookiecutter.package_name }}")
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

    if PUSH_REPO == "true":
        _underline_print("Pushing to GitHub")
        subprocess.run(["git", "push", "--set-upstream", "origin", "main"], check=True)

    _underline_print("Completed git setup")


def _error_msg(msg: str) -> str:
    error = "-" * 22 + " ERROR " + "-" * 22
    return f"{error}\n{msg}\n{'-' * len(error)}"


def main():
    """Setup CAF directory and commit to git, if enabled."""
    if CAF == "true":
        caf_setup()

    if INIT_GIT == "true":
        try:
            init_git()
        except Exception as exc:
            raise SystemExit(
                _error_msg(
                    f"Error initialising git repository: {exc}\n"
                    "Try setting init_git to False to use the template"
                    f" without setting up the git repository."
                )
            ) from exc
    elif PUSH_REPO == "true":
        raise SystemExit(
            _error_msg(
                "Cannot push repository if init_git is False, either "
                "enable init_git or disable push_repository."
            )
        )


if __name__ == "__main__":
    main()
