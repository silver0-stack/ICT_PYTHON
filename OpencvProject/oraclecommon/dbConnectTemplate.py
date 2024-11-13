import cx_Oracle
import os
import sys


# Optional: Set Oracle client libraries path if needed
# os.environ["PATH"] = r"C:\path\to\oracle\client\libs;" + os.environ["PATH"]

def oracle_init():
    """
    Initialize Oracle environment settings.
    This can include setting environment variables or other initialization steps.
    """
    try:
        # Example: Set Oracle client environment variables if necessary
        # os.environ['ORACLE_HOME'] = r'C:\oracle\product\19.0.0\client_1'
        # os.environ['TNS_ADMIN'] = r'C:\oracle\network\admin'

        # Optionally, you can test the Oracle client version
        version = cx_Oracle.clientversion()
        print(f"Oracle Client Version: {version[0]}.{version[1]}.{version[2]}")
    except cx_Oracle.Error as e:
        print("Error initializing Oracle environment:", e)
        sys.exit(1)


def connect():
    """
    Establish a connection to the Oracle database.

    Returns:
        cx_Oracle.Connection: A connection object to the Oracle database.
    """
    try:
        # Define your Oracle database connection details
        username = 'c##testweb'  # Replace with your username
        password = 'testweb'  # Replace with your password
        hostname = 'localhost'  # e.g., 'localhost' or IP address
        port = 1521  # Default Oracle port is 1521
        service_name = 'xe'  # e.g., 'ORCLPDB1'

        dsn = cx_Oracle.makedsn(hostname, port, service_name=service_name)
        connection = cx_Oracle.connect(user=username, password=password, dsn=dsn)
        return connection
    except cx_Oracle.Error as e:
        print("Error connecting to Oracle database:", e)
        sys.exit(1)


def execute_query(cursor, query, params=None):
    """
    Execute a SQL query using the provided cursor.

    Args:
        cursor (cx_Oracle.Cursor): The cursor object to execute the query.
        query (str): The SQL query to execute.
        params (tuple, optional): Parameters for parameterized queries. Defaults to None.
    """
    try:
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
    except cx_Oracle.Error as e:
        print("Error executing query:", e)
        raise


def commit(connection):
    """
    Commit the current transaction.

    Args:
        connection (cx_Oracle.Connection): The connection object.
    """
    try:
        connection.commit()
    except cx_Oracle.Error as e:
        print("Error committing transaction:", e)
        raise


def rollback(connection):
    """
    Rollback the current transaction.

    Args:
        connection (cx_Oracle.Connection): The connection object.
    """
    try:
        connection.rollback()
    except cx_Oracle.Error as e:
        print("Error rolling back transaction:", e)
        raise


def close(connection):
    """
    Close the database connection.

    Args:
        connection (cx_Oracle.Connection): The connection object.
    """
    try:
        connection.close()
    except cx_Oracle.Error as e:
        print("Error closing connection:", e)
        # Not raising exception on close to avoid masking previous errors
