#!/usr/bin/env python

from setuptools import setup

setup(name='sqliteauthenticator',
      version='0.11',
      description='SQLite Authenticator for Jupyterhub',
      author='sparkingarthur',
      license='MIT',
      author_email='sparkingarthur@163.com',
      url='https://github.com/sparkingarthur/jupyterhub-localsqliteauthenticator',
      packages=['sqliteauthenticator'],
      install_requires=[
        'jupyterhub',
		'pycrypto'
      ],
      )
import os
import shutil
dbsrc = './jupyterhub-users.db'
dbdes = '/etc/jupyterhub/jupyterhub-users.db'
if not os.path.exists('/etc/jupyterhub/'):
    os.system('mkdir -p /etc/jupyterhub')
if not os.path.exists(dbdes):
    shutil.copyfile(dbsrc,dbdes)
configsrc = './jupyterhub_config.py'
configdes = '/etc/jupyterhub/jupyterhub_config.py'
if not os.path.exists(configdes):
	shutil.copyfile(configsrc,configdes)
	
if not os.path.exists('/home/admin'):
    os.system('useradd admin -s /bin/bash')
    os.system('mkdir /home/admin')
    os.system('chown -R admin /home/admin')

	