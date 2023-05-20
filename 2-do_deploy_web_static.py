#!/usr/bin/python3
"""
This script distributes archives to your web servers
run this if env.user is not set:
     fab -f 2-do_deploy_web_static.py
     do_deploy:archive_path=versions/web_static_20170315003959.tgz
     -i my_ssh_private_key -u ubuntu

But for this script (-u) will not be included.
"""
import os
from fabric.api import put, run, env

env.hosts = ['35.175.135.243', '54.157.136.243']
env.user = 'ubuntu'


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
