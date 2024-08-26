import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'setup')))

from sql_conn import sql_server_connect

sql_server_connect()