#!/usr/bin/env python3

import os
import shutil

SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))
ROOT_DIR = os.path.join(SCRIPT_PATH, '../server')
OLD_IMPORT = 'swagger_server'
NEW_IMPORT = 'deregnet_rest'

BLACKLIST = ['swagger.yaml']

def fix_imports(old, new, root):
    for dirpath, dirnames, filenames in os.walk(root):
        if os.path.basename(dirpath) == '__pycache__':
            shutil.rmtree(dirpath)
            continue
        for fname in filenames:
            if fname in BLACKLIST:
                continue
            print(dirpath, fname)
            success = False
            filepath = os.path.join(dirpath, fname)
            with open(filepath, 'r') as fp:
                try:
                    content = fp.read()
                    content = content.replace(old, new)
                    success = True
                except:
                    continue
            if success:
                with open(filepath, 'w') as fp:
                    fp.write(content)

if __name__ == '__main__':
    fix_imports(OLD_IMPORT, NEW_IMPORT, ROOT_DIR)
