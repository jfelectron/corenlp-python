"""
This subserver scripts maintain a connection with child
processes so that our requests are not blocking

arg 1: server
arg 2: filename of tmp file

"""

import sys, jsonrpclib, os

server = jsonrpclib.Server(sys.argv[1])
filename = sys.argv[2]
with open(filename, 'r') as f:
  text = "\n".join(f.readlines())

print server.parse(text)

os.remove(filename)

