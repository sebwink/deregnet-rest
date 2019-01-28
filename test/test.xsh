import unittest

$API_ROOT='kong:8000/deregnet'

http -a test:test GET $API_ROOT/graphs
