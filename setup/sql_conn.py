import pyodbc 
import os
import sys
import logging

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'setup')))

from config import config_credentials

logging.basicConfig(level=logging.INFO)

connection_string = (
    f"DRIVER={config_credentials['Driver']};"
    f"Server={config_credentials['Server']};"
    f"Database={config_credentials['Database']};"
    f"Trusted_Connection={config_credentials['Trusted_Connection']}"
)

def sql_server_connect():
    try:
        cnxn = pyodbc.connect(connection_string)
        logging.info("Connection With SQL Server successful!")
    except Exception as e:
        logging.error(f"Connection with SQL Server failed due to {e}")
    
    return cnxn
