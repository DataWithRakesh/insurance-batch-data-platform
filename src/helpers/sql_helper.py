import pyodbc
from src.helpers.config import *
from src.utils.logger import logger

def get_connection():
    logger.info("Connecting to Azure SQL Database...")
    connection_string = (
        f"DRIVER={{ODBC Driver 18 for SQL Server}};"
        f"SERVER={SQL_SERVER};"
        f"DATABASE={SQL_DATABASE};"
        f"UID={SQL_USERNAME};"
        f"PWD={SQL_PASSWORD};"
        "Encrypt=yes;"
        "TrustServerCertificate=no;"
        
    )

    try:
        conn = pyodbc.connect(connection_string)

        logger.info("Successfully connected to Azure SQL Database.")

        return conn

    except Exception as ex:
        logger.exception(f"Database connection failed: {ex}")
        raise

def get_latest_pipeline_status(pipeline_name):
    conn = get_connection()

    cursor = conn.cursor()

    query = """
    SELECT TOP 1
           run_id,
           pipeline_name,
           status,
           start_time,
           end_time
    FROM pipeline_run
    WHERE pipeline_name = ?
    ORDER BY start_time DESC
    """

    cursor.execute(query, pipeline_name)

    row = cursor.fetchone()

    conn.close()
    
    return row
