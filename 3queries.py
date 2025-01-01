import connect_postgres_db as cdb

def execute_query(query, params=None):
    """Execute a SQL query and return the results"""
    with cdb.create_connection(cdb.db_config) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            try:
                result = cursor.fetchall()
                return result
            except cdb.psycopg2.ProgrammingError:
                # No results to fetch
                return None

queries = [
    # Get all tasks for a specific user by user_id
    "SELECT tasks.id, tasks.title, tasks.description, status.name as status FROM tasks JOIN status ON tasks.status_id = status.id WHERE tasks.user_id = 2",
    # Select tasks by a specific status
    "SELECT title FROM tasks JOIN status ON tasks.status_id = status.id WHERE status.name = 'new'",
    # Get all tasks that are not completed
    "SELECT * FROM tasks JOIN status ON tasks.status_id = status.id WHERE status.name != 'completed'",
    # Get list of tasks with no description
    "SELECT * FROM tasks WHERE description = ''",
    # Get users and their tasks in 'in progress' status
    "SELECT users.fullname, tasks.title FROM users INNER JOIN tasks ON users.id = tasks.user_id INNER JOIN status ON tasks.status_id = status.id WHERE status.name = 'in progress'",
    # Get users and the number of their tasks
    "SELECT users.fullname, COUNT(tasks.id) AS task_count FROM users LEFT JOIN tasks ON users.id = tasks.user_id GROUP BY users.id, users.fullname",
    # Data retrieval
    "SELECT * FROM users WHERE email LIKE 'example@%'",  # Find users with a specific email pattern

    # Data manipulation
    "UPDATE tasks SET status_id = (SELECT id FROM status WHERE name = 'in progress') WHERE title = 'Spiderman';",  # Update status of a specific task
    "DELETE FROM tasks WHERE id = 8",  # Delete a specific task by id
    "UPDATE users SET fullname = 'Antonio Banderas' WHERE id = 54",  # Update user name

    # Data insertion
    "INSERT INTO tasks (title, description, status_id, user_id) VALUES ('New task', 'Task description', 1, (SELECT id FROM users WHERE fullname = 'John Doe'))",  # Insert a new task for a specific user

    # Data aggregation
    "SELECT status.name, COUNT(tasks.id) AS task_count FROM tasks JOIN status ON tasks.status_id = status.id GROUP BY status.name",  # Get task count for each status

    # Using subqueries (placed at the end)
  "SELECT * FROM users WHERE id NOT IN (SELECT user_id FROM tasks)",  # Get list of users with no tasks
    "SELECT tasks.* FROM tasks JOIN users ON tasks.user_id = users.id WHERE users.email LIKE '%@example.com'",  # Get tasks assigned to users with a specific email domain
]

with cdb.create_connection(cdb.db_config) as conn:
    with conn.cursor() as cursor:
        for query in queries:
            result = execute_query(query)
            print(query)
            print(result)
            print()
