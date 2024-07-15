#!/usr/bin/python3
"""
This script generate .tgz archive from the contents of the web_static folder
"""
from fabric.api import local
import os
import time


def do_pack():
    """
    This return the archive if it hase been correct
    """
    if not os.path.exists("versions"):
        os.makedirs("versions")

    date = time.strftime("%Y%m%d%H%M%S")
    archived_path = "versions/web_stactic_{}.tgz".format(date)
    t_gzip_archive = local("tar -cvzf {} web_static".format(archived_path))

    if t_gzip_archive.succeeded:
        return archived_path
    else:
        return None
