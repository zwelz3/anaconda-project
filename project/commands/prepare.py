"""The ``prepare`` command configures a project to run, asking the user questions if necessary."""
from __future__ import absolute_import, print_function

import os
import sys

from project.plugins.requirement import RequirementRegistry
from project.prepare import prepare, UI_MODE_BROWSER
from project.project import Project


def prepare_command(dirname, ui_mode):
    """Configure the project to run.

    Returns:
        True on success.
    """
    requirement_registry = RequirementRegistry()
    project = Project(dirname, requirement_registry)
    return prepare(project, ui_mode=ui_mode)


def main(argv):
    """Start the prepare command."""
    # future: real arg parser
    if len(argv) > 1:
        dirname = argv[1]
    else:
        dirname = "."
    dirname = os.path.abspath(dirname)
    if prepare_command(dirname, ui_mode=UI_MODE_BROWSER):
        sys.exit(0)
    else:
        sys.exit(1)
