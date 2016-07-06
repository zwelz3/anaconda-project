# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Copyright © 2016, Continuum Analytics, Inc. All rights reserved.
#
# The full license is in the file LICENSE.txt, distributed with this software.
# ----------------------------------------------------------------------------
"""The ``clean`` command removes generated state."""
from __future__ import absolute_import, print_function

from conda_kapsel.project import Project
from conda_kapsel.prepare import prepare_without_interaction
from conda_kapsel.provide import PROVIDE_MODE_CHECK
from conda_kapsel.commands import console_utils
import conda_kapsel.project_ops as project_ops


def clean_command(project_dir):
    """Clean up generated state.

    Returns:
        exit code
    """
    project = Project(project_dir)
    result = prepare_without_interaction(project, mode=PROVIDE_MODE_CHECK)
    status = project_ops.clean(project, result)
    if status:
        print(status.status_description)
        return 0
    else:
        console_utils.print_status_errors(status)
        return 1


def main(args):
    """Start the clean command and return exit status code."""
    return clean_command(args.directory)
