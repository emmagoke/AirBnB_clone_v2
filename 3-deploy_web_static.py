#!/usr/bin/python3
"""
This script (based on the file 2-do_deploy_web_static.py) that creates and
distributes an archive to your web servers
"""
import os
from datetime import datetime
from fabric.api import env, run, put, local

env.hosts = ['35.175.135.243', '54.157.136.243']


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


def do_deploy(archive_path):
    """ this function distributes archive on my web servers """

    if not os.path.exists(archive_path):
        return False

    try:
        data_path = "/data/web_static/releases"
        archive_name = archive_path.split('/')[-1]
        ex_name = archive_name.split(".")[0]

        put(archive_path, '/tmp/')
        run("mkdir -p {0}/{1}/".format(data_path, ex_name))
        run("tar -xzf /tmp/{} -C {}/{}/".format(archive_name,
            data_path, ex_name))
        run("rm /tmp/{}".format(archive_name))
        run("mv {0}/{1}/web_static/* {0}/{1}/".format(data_path, ex_name))
        run("rm -rf {}/{}/web_static".format(data_path, ex_name))
        run("rm -rf /data/web_static/current")
        run("ln -sf {}/{}/ /data/web_static/current".format(data_path,
            ex_name))

        return True
    except Exception as e:
        print(e)
        return False


def deploy():
    """ that creates and distributes an archive to your web servers """

    archive_pack = do_pack()

    if archive_pack:
        result = do_deploy(archive_pack)
        return result
    else:
        return False
