#!/usr/bin/env python3

import os
import re

SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))
ROOT_DIR = os.path.join(SCRIPT_PATH, '../server/controllers')

def get_controller_call(func, fname):
    fstem = fname.split('.')[0]
    controller_name = ''.join(
        [part[0].upper() + part[1:] for part in fstem.split('_')]
    )
    return '{}.{}'.format(controller_name, func)

def strip_default_args_from(args):
    args = re.sub(
        r'=[^,]*',
        '',
        args,
    )
    return re.sub(
        r'=[^\)]*',
        '',
        args,
    )

def get_import(fname):
    fstem = fname.split('.')[0]
    controller_name = ''.join(
        [part[0].upper() + part[1:] for part in fstem.split('_')]
    )
    controller_file = '_'.join(fstem.split('_')[:-1])+'s'
    return 'from deregnet_rest.controllers_impl.{} import {}'.format(
        controller_file, controller_name
    )


def populate_controllers(root):
    for dirpath, dirnames, filenames in os.walk(root):
        if os.path.basename(dirpath) == '__pycache__':
            continue
        for fname in filenames:
            if fname == '__init__.py':
                continue
            filepath = os.path.join(dirpath, fname)
            with open(filepath, 'r') as fp:
                def sub(match):
                    func = match.group(1)
                    args = match.group(2)
                    stripped_args = strip_default_args_from(args)
                    body_and_return = match.group(3)
                    return 'def {}({}){}{}({})'.format(
                        func,
                        args,
                        body_and_return,
                        get_controller_call(func, fname),
                        stripped_args,
                    )
                content = fp.read()
                content = re.sub(
                    r'^def ([\w]+)\(([^\)]*)\)(.*?)(\'do some magic!\')',
                    sub,
                    content,
                    flags=re.MULTILINE | re.DOTALL,
                )
                def sub2(match):
                    rest = match.group(1)
                    return '{}\n\n{}'.format(get_import(fname), rest)
                content = re.sub(
                    r'(^def.*$)',
                    sub2,
                    content,
                    flags=re.MULTILINE | re.DOTALL,
                )

            with open(filepath, 'w') as fp:
                fp.write(content)

if __name__ == '__main__':
    populate_controllers(ROOT_DIR)
