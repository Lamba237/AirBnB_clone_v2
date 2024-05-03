#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py)
"""
from fabric.api import env, put, run, sudo
from os.path import exists


env.hosts = ['xx-web-01', 'xx-web-02']


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
    except:
        return None


def do_deploy(archive_path):
    """
    Fabric script that distributes an archive
    to your web servers, using the function do_deploy:
    """

    if not exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp/')

        archive_filename = archive_path.split('/')[-1]
        folder_name = archive_filename.split('.')[0]

        run('mkdir -p /data/web_static/releases/{}/'.format(folder_name))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(
             archive_filename, folder_name))
        run('rm /tmp/{}'.format(archive_filename))
        run('rm -rf /data/web_static/current')
        ln_file = 'ln -s /data/web_static/releases/{}/'.format(folder_name)
        run('{} /data/web_static/current'.format(ln_file))
        return True
    except Exception as e:
        print(e)
        return False
