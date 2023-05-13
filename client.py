##################################################################
# Project:  CSE-5306 Multi-Threaded Server
# Date:     Friday 16 September 2022
# Authors:  Prithvi Bhat (pnb3598@mavs.uta.edu)
##################################################################

import os
import threading
import xmlrpc.client
import sys
from array import *

PORT                = 8000                      # Port to bind socket to
SERVER_HOST         = "0.0.0.0"                 # Server Host address


def Main():
    server_endpoint = 'http://{}:{}'.format(SERVER_HOST, PORT)      # Set an endpoint for the client to communicate to

    server_proxy = xmlrpc.client.ServerProxy(server_endpoint)       # Set server Proxy
    multicall = xmlrpc.client.MultiCall(server_proxy)               # Initiate multicall

    while True:
        operation = input("Select operation (ADD (INTEGERS) | SORT (INTEGER ARRAY)): ")     # Take user choice of operation

        if operation == "ADD":
            integer1 = int(input("Enter integer 1: "))                                      # Read two integers to add
            integer2 = int(input("Enter integer 2: "))
            multicall.add(integer1, integer2)                                               # Call RPC to perform operation

        if operation == "SORT":
            user_array=[]
            size = int(input("Enter number of elements sort: "))                            # Input size of array from user
            print("Enter elements: \n")
            for i in range(0, size):
                user_array.append(int(input()))                                             # Read array elements from user
            multicall.sort(user_array)                                                      # Call RPC to perform sort operation

        result = multicall()                                                                # Encapsulate multiple RPC calls into a single request
        if operation == "ADD":
            print("Sum of input numbers is %d" % tuple(result))
        elif operation == "SORT":
            print("Sorted Array is %s" % list(result))

if __name__ == '__main__':
    Main()
