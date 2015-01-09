# -*- coding: utf-8 -*-
import sys
import os
import time

from fabric.api import settings, run, env, local

#Change this configuration
from django.conf import settings
sys.path.insert(0, os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2]))

env.project_name = 'm2re'
#env.hosts = ['host1']
# env.user = 'm2re'
# env.password = 'm2re_2015'

# env.date = time.strftime('%Y%m%d%H%M%S')
# os.environ['DJANGO_SETTINGS_MODULE'] = '%(project_name)s.settings' % env

# env.db_name = settings.DATABASES['default']['NAME']
# env.db_user = settings.DATABASES['default']['USER']
# env.db_password = settings.DATABASES['default']['PASSWORD']
# env.db_host = settings.DATABASES['default']['HOST']
# env.db_port = settings.DATABASES['default']['PORT']


def runserver(port='8012', ip='0.0.0.0'):
    local('./manage.py runserver %s:%s --settings=%s.local_settings' % (ip, port, env.project_name))


def hello(name='world'):
    print(u'hello {}'.format(name))
