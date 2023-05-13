##################################################################
# Project:  CSE-5306 Multi-Threaded Server
# Date:     Friday 16 September 2022
# Authors:  Prithvi Bhat (pnb3598@mavs.uta.edu)
##################################################################

from code import interact
import os
import threading
from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
import sys

PORT                = 8000                      # Port to bind socket to
SERVER_HOST         = "0.0.0.0"                 # Server Host address

def addition(integer1, integer2):
    return integer1 + integer2                  # Return sum of two integers

def sort(array):
    return (sorted(array))                      # Return sorted array


def Main():
    server = SimpleXMLRPCServer((SERVER_HOST, PORT))
    print("Server online\nListening on port [" + str(PORT) + "]")
    server.register_multicall_functions()                           # Initiate multicall requests
    server.register_function(addition, 'add')                       # Register RPCs
    server.register_function(sort, 'sort')
    try:
        server.serve_forever()                                      # Run server and broadcast RPCs infinitely
    except KeyboardInterrupt:
        print("Killing Server")

if __name__ == '__main__':
    Main()