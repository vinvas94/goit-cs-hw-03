import psycopg2
from contextlib import contextmanager

def create_connection(db_config):
    """Creates a connection to a PostgreSQL database using the provided configuration.

    Args:
        db_config (dict): A dictionary containing database connection parameters.

    Yields:
        psycopg2.connection: A database connection object.
    """

    conn = psycopg2.connect(**db_config)
    try:
        yield conn
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()

# Database connection configuration
db_config = {
    'dbname': 'my_project_db',
    'user': 'postgres',
    'password': 'my_strong_password',
    'host': 'localhost',
    'port': '5432'
}
