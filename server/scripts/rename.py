#!/usr/bin/env python3

import os
import sys

OLD_NAME = 'swagger_server'
NEW_NAME = 'deregnet_rest'
DIR_BLACKLIST = ['.tox', 'scripts', '.git']

if len(sys.argv) > 1:
    ROOT_DIR = sys.argv[1]
else:
    ROOT_DIR = '.'

def rename(old, new, root):
    for dirpath, dirnames, filenames in os.walk(root):
        if '/' in dirpath and dirpath.split('/')[1] in DIR_BLACKLIST:
            continue
        print(dirpath, dirnames, filenames)
        for fname in filenames:
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
    rename(OLD_NAME, NEW_NAME, ROOT_DIR)
    os.rename(OLD_NAME, NEW_NAME)
