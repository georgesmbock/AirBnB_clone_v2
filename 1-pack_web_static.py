#!/usr/bin/python3
"""
fafric script that generates a /tgz from the contents of web_static
"""
from fabric.api import local
import time
import os


def do_pack():
    """
    return the archive path if archive has bbeenn correctly
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
