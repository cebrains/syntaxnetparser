#!/usr/bin/env python
# coding=utf8
"""
# Author: f
# Created Time : Thu 18 May 2017 07:50:05 PM CST

# File Name: parser.py
# Description:

"""

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import base
from syntaxnet.textparser import TextParser
from argparse import ArgumentParser
import os
from os.path import join, dirname, abspath
import time
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

MODEL_DIR = join(dirname(abspath(__file__)), 'data')
POS_PARAM = '128-0.08-400-0.9-0'
PARSER_PARAM = '512x512-0.02-100-0.9-0'



if __name__=="__main__":
    parser = TextParser(sys.argv[1], POS_PARAM, PARSER_PARAM, '256,256', '512,512')
    text = u'左上肺舌段、左下肺炎症并含气不全较前改善。'
    text1 = u'左上肺舌段、左下肺炎症,1,2,3,4,6,7,8,9,10,11'
    text_list = []
    start_time = time.time()
    for i in range(0, 100):
        if i % 2 == 0:
            input = [text] * 4
        else:
            input = [text1] * 6

        parse_result = parser.parse(input)
        for item in parse_result:
            print item
        print '----------------------'
    end_time = time.time()
    print end_time-start_time
