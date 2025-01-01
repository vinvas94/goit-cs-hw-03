import connect_postgres_db as cdb

# SQL commands to create tables
create_users_table = """
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    fullname VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);
"""

create_status_table = """
CREATE TABLE IF NOT EXISTS status (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL
);
"""

create_tasks_table = """
CREATE TABLE IF NOT EXISTS tasks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    status_id INTEGER REFERENCES status(id) ON DELETE CASCADE,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

# Insert initial status data
insert_status_data = """
INSERT INTO status (name)
VALUES
    ('new'),
    ('in progress'),
    ('completed')
ON CONFLICT (name) DO NOTHING;
"""

# Execute SQL commands
def create_tables():
    with cdb.create_connection(cdb.db_config) as conn:
        with conn.cursor() as cursor:
            for query in (
                create_users_table,
                create_status_table,
                insert_status_data,
                create_tasks_table
            ):
                cursor.execute(query)
                print(f"{query.split()[0]} table created successfully.")

if __name__ == "__main__":
    create_tables()
