# -*- coding: utf-8 -*-
"""Cookiecutter hook script running before user prompts."""

##### IMPORTS #####
import json
import pathlib

##### CONSTANTS #####

JSON_PATH = pathlib.Path("cookiecutter.json")
README_PATH = pathlib.Path("README.md")


##### CLASSES & FUNCTIONS #####


def get_template_details() -> str:
    """Load template details section from root README."""
    read = False
    text = []
    with open(README_PATH, "rt", encoding="utf-8") as file:
        for line in file:
            if line.lower().strip() == "## template details":
                read = True

            if read:
                text.append(line)

    return "".join(text)


def main():
    """Fill in the "_template_details" variable in cookiecutter.json."""

    with open(JSON_PATH, "rt", encoding="utf-8") as file:
        data = json.load(file)

    data["_template_details"] = get_template_details()

    with open(JSON_PATH, "wt", encoding="utf-8") as file:
        json.dump(data, file)


if __name__ == "__main__":
    main()
