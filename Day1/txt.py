import psycopg2
import sys

class TodoAppPG:
    def __init__(self, db_params):
        try:
            # Connect to PostgreSQL server
            self.conn = psycopg2.connect(**db_params)
            self.cursor = self.conn.cursor()
            self.setup_database()
        except Exception as e:
            print(f"Failed to connect to database: {e}")
            sys.exit()

    def setup_database(self):
        """Create the tasks table with auto-incrementing SERIAL ID."""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id SERIAL PRIMARY KEY,
                task TEXT NOT NULL,
                priority INTEGER NOT NULL,
                status TEXT DEFAULT 'Pending'
            )
        ''')
        self.conn.commit()

    def add_task(self, task, priority_str):
        """Insert a task with mapped priority."""
        priorities = {"high": 1, "medium": 2, "low": 3}
        priority = priorities.get(priority_str.lower(), 3)
        
        # Use parameterized queries to prevent SQL injection
        self.cursor.execute(
            "INSERT INTO tasks (task, priority) VALUES (%s, %s)", 
            (task, priority)
        )
        self.conn.commit()
        print(f"Task added: {task}")

    def view_tasks(self):
        """Fetch tasks sorted by priority (ASC)."""
        self.cursor.execute("SELECT id, task, priority, status FROM tasks ORDER BY priority ASC")
        tasks = self.cursor.fetchall()
        
        if not tasks:
            print("\nNo tasks found.")
            return

        priority_map = {1: "High", 2: "Medium", 3: "Low"}
        print("\n--- Current Tasks ---")
        for t in tasks:
            print(f"ID: {t[0]} | Task: {t[1]:<20} | Priority: {priority_map[t[2]]:<7} | Status: {t[3]}")

    def complete_task(self, task_id):
        """Update task status to 'Completed'."""
        self.cursor.execute("UPDATE tasks SET status = 'Completed' WHERE id = %s", (task_id,))
        if self.cursor.rowcount == 0:
            print(f"Task ID {task_id} not found.")
        else:
            self.conn.commit()
            print(f"Task {task_id} marked as completed.")

    def delete_task(self, task_id):
        """Delete task by ID."""
        self.cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
        if self.cursor.rowcount == 0:
            print(f"Task ID {task_id} not found.")
        else:
            self.conn.commit()
            print(f"Task {task_id} deleted.")

    def close(self):
        self.cursor.close()
        self.conn.close()

def main():
    # Database connection parameters (update with your actual credentials)
    db_config = {
        "dbname": "todo_db",
        "user": "postgres",
        "password": "yourpassword",
        "host": "localhost",
        "port": "5432"
    }
    
    app = TodoAppPG(db_config)
    
    while True:
        print("\n1. Add | 2. View | 3. Complete | 4. Delete | 5. Exit")
        choice = input("Select: ")

        try:
            if choice == '1':
                task = input("Task: ")
                priority = input("Priority (high/medium/low): ")
                app.add_task(task, priority)
            elif choice == '2':
                app.view_tasks()
            elif choice == '3':
                tid = int(input("Task ID: "))
                app.complete_task(tid)
            elif choice == '4':
                tid = int(input("Task ID: "))
                app.delete_task(tid)
            elif choice == '5':
                app.close()
                sys.exit()
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
