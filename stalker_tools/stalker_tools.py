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
