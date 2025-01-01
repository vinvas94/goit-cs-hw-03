-- Get all tasks for a specific user (with ID = 2)
SELECT tasks.id, tasks.title, tasks.description, status.name AS status
FROM tasks
JOIN status ON tasks.status_id = status.id
WHERE tasks.user_id = 2;

-- Get tasks with the status "new"
SELECT title
FROM tasks
JOIN status ON tasks.status_id = status.id
WHERE status.name = 'new';

-- Get all incomplete tasks
SELECT * 
FROM tasks
JOIN status ON tasks.status_id = status.id
WHERE status.name != 'completed';

-- Get tasks without a description
SELECT * FROM tasks WHERE description = '';

-- Get users and their tasks in "in progress" status
SELECT users.fullname, tasks.title
FROM users
INNER JOIN tasks ON users.id = tasks.user_id
INNER JOIN status ON tasks.status_id = status.id
WHERE status.name = 'in progress';

-- Get users and the count of their tasks
SELECT users.fullname, COUNT(tasks.id) AS task_count
FROM users
LEFT JOIN tasks ON users.id = tasks.user_id
GROUP BY users.id, users.fullname;

-- Find users with email starting with "example@"
SELECT * FROM users WHERE email LIKE 'example@%';

-- Update the status of the task "Spiderman" to "in progress"
UPDATE tasks
SET status_id = (SELECT id FROM status WHERE name = 'in progress')
WHERE title = 'Spiderman';

-- Delete the task with ID = 8
DELETE FROM tasks WHERE id = 8;

-- Update the full name of the user with ID = 54 to "Antonio Banderas"
UPDATE users SET fullname = 'Antonio Banderas' WHERE id = 54;

-- Insert a new task for the user "John Doe"
INSERT INTO tasks (title, description, status_id, user_id)
VALUES ('New task', 'Task description', 1, (SELECT id FROM users WHERE fullname = 'John Doe'));

-- Count tasks for each status
SELECT status.name, COUNT(tasks.id) AS task_count
FROM tasks
JOIN status ON tasks.status_id = status.id
GROUP BY status.name;

-- Find users without any tasks
SELECT * FROM users WHERE id NOT IN (SELECT user_id FROM tasks);

-- Find tasks assigned to users with email domain "@example.com"
SELECT tasks.*
FROM tasks
JOIN users ON tasks.user_id = users.id
WHERE users.email LIKE '%@example.com';
