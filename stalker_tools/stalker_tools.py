# -*- coding: utf-8 -*-

'''
A Stalker tool
'''

import json
import os
import requests
import subprocess
from configobj import ConfigObj

# CONFIG = ConfigObj('//.../stalker_tools.conf')

def path_expanduser(path='~/'):
    '''
    Return the user folder path
    '''
    return os.path.expanduser(path)

def bash(cmd=None):
    '''
    bash function to execute pure bash commands

    Parameters
    ----------
    cmd : str
        the string value with the bash line code
    '''
    if not isinstance(cmd, str):
        return
    return subprocess.check_output(cmd, shell=True)

def cmd_host(domain=None):
    '''
    bash function to execute pure bash commands

    Parameters
    ----------
    domain : str
        domain string
    '''
    if not isinstance(domain, str):
        return
    return bash('host {}'.format(domain))

def list_http_headers(domain=None):
    '''
    function to list all http headers of the domain

    Parameters
    __________
    domain : str
        domain string to be inspectected
    '''
    http_header = requests.head(domain)

    formated_data_http_header = dict()

    formated_data_http_header['status_code'] = http_header.status_code
    formated_data_http_header['server'] = http_header.headers.get('server', default = 'not found')
    formated_data_http_header['platform_vtex'] = http_header.headers.get('powered', default = 'false')

    return formated_data_http_header

class StalkerTools():
    '''
    StalkerTools class to facilitate api manipulation

	Parameters
    ----------
    domain_list : list
        the string contains the password value.
    '''
    def __init__(self, domain_list):
        # import pdb; pdb.set_trace()
        return self
