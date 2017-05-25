#!/usr/bin/env python
# coding=utf8
"""
# Author: f
# Created Time : Fri 19 May 2017 02:25:40 PM CST

# File Name: __init__.py
# Description:

"""

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
import base
from syntaxnet.textparser import TextParser
from os.path import join, dirname, abspath

def setLogLevel(level):
    '''
        @Brief: set log level for tensorflow
    '''
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = str(level)


setLogLevel(2)

