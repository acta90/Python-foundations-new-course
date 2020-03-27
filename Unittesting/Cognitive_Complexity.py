import os
import json
from contextlib import contextmanager
import hcl

cfn = [".json", ".template", ".yaml", ".yml"]
tf = ["tf"]


def _file_paths(directory):
    for root, dirs, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(root, filename)
            if os.path.isfile(file_path):
                yield file_path


def file_handler(dir):
    for file_path in _file_paths(dir):
        _handle_file(file_path)


def _handle_file(file_path):
    base, extension = os.path.splitext(file_path)
    handler = _extension_handlers.get(extension, _null_handler)
    with open(file_path) as file_object:
        with _translate_error(ValueError, SystemExit):
            handler(file_object)


def _handle_cfn(file_object):

    file_contents = file_object.read()
    if "AWSTemplateFormatVersion" in file_contents:
        data = json.dumps(file_contents)
        print(data)


def _handle_tf(file_object):

    obj = hcl.load(file_object)
    data = json.dumps(obj)
    print(data)


def _null_handler(file_object):
    pass


@contextmanager
def _translate_error(from_error, to_error):
    try:
        yield
    except from_error as error:
        raise to_error(error)


_extension_handlers = {'.json': _handle_cfn,
                       '.template': _handle_cfn,
                       '.yaml': _handle_cfn,
                       '.yml': _handle_cfn,
                       '.tf': _handle_tf}