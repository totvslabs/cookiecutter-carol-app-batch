#!/usr/bin/env python
import http
import os
import platform
import urllib

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))

def post_ga_data():
    params = urllib.urlencode({
        'v': 1,
        'tid': 'UA-144583662-1',
        'uid': '{{ cookiecutter.email }}',
        't' : 'event',
        'ec': 'carol_cookiecuter',
        'ea': 'new_batch_project',
        'an': 'cookiecutter-carol-app-batch',
        'cd1': 'tenant',
        'cm1': '{{ cookiecutter.carol_app_tenant }}',
        'cd2': 'project',
        'cm2': '{{ cookiecutter.project_name }}',
        'cd3': 'os',
        'cm3': platform.system(),
        'cd4': 'python_version',
        'cm4': platform.python_version()
    })

    connection = http.client.HTTPConnection('www.google-analytics.com')
    connection.request('POST', '/collect', params)

if __name__ == '__main__':
    pass