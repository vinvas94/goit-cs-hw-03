import connect_postgres_db as cdb
from faker import Faker

# Initialize Faker
fake = Faker()

def seed_users(cursor, num_users=10):
    """Seed users table with fake data"""
    try:
        for _ in range(num_users):
            fullname = fake.name()
            email = fake.unique.email()
            cursor.execute("INSERT INTO users (fullname, email) VALUES (%s, %s)", (fullname, email))
    except Exception as e:
        print(f"Error seeding users: {e}")

def seed_tasks(cursor, num_tasks=30):
    """Seed tasks table with fake data"""
    try:
        cursor.execute("SELECT id FROM users")
        user_ids = [row[0] for row in cursor.fetchall()]

        cursor.execute("SELECT id FROM status")
        status_ids = [row[0] for row in cursor.fetchall()]

        for _ in range(num_tasks):
            title = fake.sentence(nb_words=6)
            description = fake.text()
            status_id = fake.random.choice(status_ids)
            user_id = fake.random.choice(user_ids)
            cursor.execute("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)", 
                            (title, description, status_id, user_id))
    except Exception as e:
        print(f"Error seeding tasks: {e}")

with cdb.create_connection(cdb.db_config) as conn:
    with conn.cursor() as cursor:
        seed_users(cursor)
        print("Users table seeded successfully.")
        
        seed_tasks(cursor)
        print("Tasks table seeded successfully.")
