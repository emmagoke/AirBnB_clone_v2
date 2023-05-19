#!/usr/bin/python3
"""
This is a Fabric script that generates a .tgz archive from the contents
of the web_static folder
"""
import os
from datetime import datetime
from fabric.api import local


def do_pack():
    """ This function creates an archive based on the tar command. """

    try:
        if not os.path.isdir('versions'):
            local('mkdir -p versions')

        today_date = datetime.now().strftime("%Y%m%d%H%M%S")
        output_file = "versions/web_static_{}.tgz".format(today_date)

        local("tar -cvzf {} web_static".format(output_file))
        return output_file
    except Exception:
        return None
