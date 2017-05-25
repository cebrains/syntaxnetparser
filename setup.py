# encoding=utf8

""" The syntaxnetparser setup script
    Author: qiupengfei
    Created Time : 三  1/20 20:11:05 2016

    File Name: setup.py
    Description:

"""

import sys
reload(sys)
sys.setdefaultencoding("utf8")

import os
import os.path

PackageDirName = "syntaxnetparser"
MetaFileName = "__buildmeta__.py"

from setuptools import setup, find_packages

requirements = [ x.strip() for x in open("requirements.txt").readlines() ]

# Create build meta
buildMetaFile = os.path.join(os.path.dirname(os.path.abspath(__file__)), PackageDirName, MetaFileName)
try:
    branch, commit, tag, time = os.environ.get("CI_BRANCH"), os.environ.get("CI_COMMIT"), os.environ.get("CI_TAG"), os.environ.get("CI_TIME")
    with open(buildMetaFile, "wb") as fd:
        print >>fd, '''#encoding=utf8
buildBranch = """%s"""
buildCommit = """%s"""
buildTag    = """%s"""
buildTime   = """%s"""
''' % (branch or "", commit or "", tag or "", time or "")
    setup(
        name = "syntaxnetparser",
        version = tag,
        author = "qiupengfei",
        author_email = "qiupengfei@rxthinking.com",
        url = "https://github.com/penfree/syntaxnetparser",
        packages = find_packages(),
        include_package_data = True,
        package_data = { "": "*" },
        install_requires = requirements,
        description = "Syntaxnet model predict",
        long_description = open("README.md").read()
    )
finally:
    # Remove generated files
    os.system("rm -f %s" % buildMetaFile)
