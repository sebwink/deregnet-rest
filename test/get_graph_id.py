import sys
import json

with open(sys.argv[1]) as fp:
    id =json.load(fp)['id']

sys.stdout.write(id)
