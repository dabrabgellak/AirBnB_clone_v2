#!/usr/bin/python3
# Distributes an archive to the web servers.

import os
import zipfile
from fabric.operations import put, run


def do_deploy(archive_path):
    """ Distributes an archive to the web servers """

    if not os.path.isdir("archive_path"):
        return False

    put("archive_path", "/tmp/")

    with zipfile. ():
