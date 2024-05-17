#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py)
"""
from fabric.api import env, put, run, sudo
from os.path import exists


env.hosts = ['18.233.63.243', '35.168.7.222']
env.uer = 'ubuntu'


def do_pack():

    """
    this function is use to generate a .tgz file
    """
    try:
        local('mkdir -p versions')
        archive_path = 'versions/web_static_{}.tgz'.format(
            datetime.now().strftime('%Y%m%d%H%M%S'))
        local('tar -cvzf {} web_static'.format(archive_path))
        print('web_static packed: {} -> {}'.format(archive_path,
              os.path.getsize(archive_path)))
    except Exception:
        return None


def do_deploy(archive_path):
    """
    Fabric script that distributes an archive
    to your web servers, using the function do_deploy:
    """

    if not exists(archive_path):
        return False
    fileName = archive_path.split('/')[1]
    filePath = '/data/web_static/releases/'
    releasePath = filePath + fileName[:-4]

    try:
        put(archive_path, '/tmp/')
        run('mkdir -p {}'.format(releasePath))
        run('tar -xzf /tmp/{} -C {}'.format(fileName, releasePath))
        run('rm /tmp/{}'.format(fileName))
        run('mv {}/web_static/* {}/'.format(releasePath, releasePath))
        run('rm -rf {}/web_static'.format(releasePath))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(releasePath))
        print('New version deployed!')
        return True
    except Exception:
        return False
