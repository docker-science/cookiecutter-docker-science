# -*- coding: utf-8 -*-

import os
import re

from binaryornot.check import is_binary
from io import open

RE_OBJ = re.compile('{{(\s?cookiecutter)[.](.*?)}}')


def build_files_list(root_dir):
    return [
        os.path.join(dirpath, file_path)
        for dirpath, _, files in os.walk(root_dir)
        for file_path in files
    ]


def check_paths(paths):
    for path in paths:
        if is_binary(path):
            continue
        for line in open(path, 'r', encoding="latin-1"):
            match = RE_OBJ.search(line)
            msg = 'variable not replaced in {}'
            assert match is None, msg.format(path)


def test_default_configuration(cookies, context={}):
    result = cookies.bake(extra_context=context)
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == 'project_name'
    assert result.project.isdir()
    paths = build_files_list(str(result.project))

    assert paths
    check_paths(paths)


def test_custom_configuration(cookies, context={'project_name': 'ml project'}):
    result = cookies.bake(extra_context=context)
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == 'ml_project'  # note formatted
    assert result.project.isdir()
    paths = build_files_list(str(result.project))

    assert paths
    check_paths(paths)
