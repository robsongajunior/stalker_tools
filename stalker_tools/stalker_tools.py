# -*- coding: utf-8 -*-

'''
A Stalker tool
'''

import os
import json
import requests
from configobj import ConfigObj

CONFIG = ConfigObj('/etc/azion/stalker_tools.conf')

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
