#!/usr/bin/python3
"""
Fabric script that creates and distributes
an archive to your web servers, using the function deploy:
"""
from fabric.api import env, put, run, sudo
from os.path import exists


env.hosts = ['18.233.63.243', '35.168.7.222']
env.uer = 'ubuntu'


def do_clean(number=0):
    ''' Removes out of date archives locally and remotely '''
    number = int(number)
    if number == 0:
        number = 2
    else:
        number += 1

    local('cd versions; ls -t | tail -n +{} | xargs rm -rf'
          .format(number))
    releases_path = '/data/web_static/releases'
    run('cd {}; ls -t | tail -n +{} | xargs rm -rf'
        .format(releases_path, number))


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
    except:
        return False

def deploy():
    """
    creates and distribute an archive to my web server
    """

    created_archive = do_pack()
    if not created_archive:
        return False

    return do_deploy(created_archive)
