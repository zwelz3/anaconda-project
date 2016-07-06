# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Copyright © 2016, Continuum Analytics, Inc. All rights reserved.
#
# The full license is in the file LICENSE.txt, distributed with this software.
# ----------------------------------------------------------------------------
"""The ``archive`` command makes an archive of the project."""
from __future__ import absolute_import, print_function

from conda_kapsel.project import Project
from conda_kapsel.commands import console_utils
import conda_kapsel.project_ops as project_ops


def archive_command(project_dir, archive_filename):
    """Make an archive of the project.

    Returns:
        exit code
    """
    project = Project(project_dir)
    status = project_ops.archive(project, archive_filename)
    if status:
        for line in status.logs:
            print(line)
        print(status.status_description)
        return 0
    else:
        console_utils.print_status_errors(status)
        return 1


def main(args):
    """Start the archive command and return exit status code."""
    return archive_command(args.directory, args.filename)
