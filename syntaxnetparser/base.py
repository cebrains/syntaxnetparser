#!/usr/bin/env python

import os
import re
import tempfile
import shutil
import sys
import subprocess
import zipfile
import platform
from os.path import join, dirname, abspath

work_dir = dirname(abspath(__file__))


def CreatePythonPathEntries(python_imports, module_space):
    parts = python_imports.split(':');
    return [module_space] + ["%s/%s" % (module_space, path) for path in parts]


def FindModuleSpace():
    # Follow symlinks, looking for my module space
    linux_version = platform.linux_distribution()
    if linux_version[0].lower() == 'ubuntu' and linux_version[1].startswith('14'):
        return join(work_dir, 'runfiles.ubuntu14')
    elif linux_version[0].lower() == 'ubuntu' and linux_version[1].startswith('16'):
        return join(work_dir, 'runfiles.ubuntu16')
    else:
        raise ValueError('unsupported linux version, %s' % str(linux_version))


def GetRepositoriesImports(module_space, import_all):
    if import_all:
        repo_dirs = [os.path.join(module_space, d) for d in os.listdir(module_space)]
        return [d for d in repo_dirs if os.path.isdir(d)]
    return [os.path.join(module_space, "__main__")]


module_space = FindModuleSpace()

python_imports = 'protobuf/python'
python_path_entries = CreatePythonPathEntries(python_imports, module_space)
python_path_entries += GetRepositoriesImports(module_space, True)
for p in python_path_entries:
    sys.path.insert(0, p)
reload(sys)
