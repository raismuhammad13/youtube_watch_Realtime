#!/usr/bin/env python
import os
import sys

try:
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'setup')))
    from sql_conn import sql_server_connect
except ImportError as e:
    print(f"Error importing module: {e}")
    sys.exit(1)

print("############################hello this is a spark code running ############################")
sql_server_connect()



