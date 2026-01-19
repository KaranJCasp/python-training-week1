import psycopg2


class Todo_pg:
    def __init__(self, db_params):
        try:
            self.conn = psycopg2.connect(**db_params)
            self.cursor = self.conn.cursor()
            self.Todo_create_Table()
        except Exception as e:
            print(f"Failed to connect to database: {e}")

    def Todo_create_Table(self):
        try:
            sqlQuery="""CREATE TABLE IF NOT EXISTS TODO(
            TODO_ID SERIAL PRIMARY KEY,
            TITLE VARCHAR(100),
            DESCRIPTION VARCHAR(100),
            PRIORITY INTEGER NOT NULL,
            STATUS TEXT DEFAULT 'Pending',
            STATUS_DELETE VARCHAR(100) DEFAULT 'NO',
            CREATED_AT TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UPDATED_AT TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );"""
            self.cursor.execute(sqlQuery)
            print("Table created successfully")
            self.conn.commit()

        except psycopg2.Error as e:
                print(f"I can't create or access the books database: {e}")
                if self.conn:
                    self.conn.rollback()
    
    def Insert_Todo(self,TITLE,DESCRIPTION,PRIORITY_STR):
        try:
            priorities = {"high": 1, "medium": 2, "low": 3}
            PRIORITY=priorities.get(PRIORITY_STR.lower(), 3)
        
            self.cursor.execute(
                "INSERT INTO TODO (TITLE, DESCRIPTION,PRIORITY) VALUES (%s, %s,%s)", 
                (TITLE,DESCRIPTION,PRIORITY)
            )
            self.conn.commit()

            print(f"Task added: {TITLE}")
        except psycopg2.Error as e:
            print(f"I can't create or access the books database: {e}")
            if self.conn:
                self.conn.rollback()
    def Read_todo(self):
        
        try:
            sqlquery="""SELECT TODO_ID, TITLE, DESCRIPTION, PRIORITY, STATUS, STATUS_DELETE 
                FROM TODO ORDER BY PRIORITY ASC;
                """
            self.cursor.execute(sqlquery)
            tasks = self.cursor.fetchall()
            if not tasks:
                print("\nNo tasks found.")
                return

            print("\n--- Current Tasks ---")
            for t in tasks:
        
                print(t)
                
                self.conn.commit()

        except psycopg2.Error as e :
            print(f"I can't create or access the books database: {e}")
            if self.conn:
                self.conn.rollback()
    def complete_task(self, task_id):
        """Update task status to 'Completed'."""
        self.cursor.execute("UPDATE TODO SET STATUS = 'Completed' WHERE TODO_ID = %s", (task_id,))
        if self.cursor.rowcount == 0:
            print(f"Task ID {task_id} not found.")
        else:
            self.conn.commit()
            print(f"Task {task_id} marked as completed.")
    def Delete_todo(self,task_id):
        self.cursor.execute("UPDATE TODO SET STATUS_DELETE = 'Deleted' WHERE TODO_ID = %s", (task_id,))
        if self.cursor.rowcount == 0:
            print(f"Task ID {task_id} not found.")
        else:
            self.conn.commit()
            print(f"Task {task_id} deleted.")
    def close(self):
        if self.cur is not None:
            self.cur.close()
            print('cursor closed')
        if self.conn is not None:
            self.conn.close()
            print("database connection closed")
def main():
    db_params = {
        'host': 'localhost',
        'database': 'Todo_database',
        'user': 'jenil',
        'password': 'Jenil@jcasp',
        'port': '5432'
    }
    
    app = Todo_pg(db_params)
    while True:
        print("\n1. Add | 2. View | 3. Complete | 4. Delete | 5. Exit")
        choice = input("Select: ")

        if choice == '1':
            TITLE = input("TITLE: ")
            DESCRIPTION=input("Enter description: ")
            PRIORITY_STR = input("Priority (high/medium/low): ")
            app.Insert_Todo(TITLE, DESCRIPTION,PRIORITY_STR)

        elif(choice=='2'):
            app.Read_todo()
        elif(choice == '3'):
            tid = int(input("Task ID: "))
            app.complete_task(tid)
        elif(choice == '4'):
            tid = int(input("Task ID: "))
            app.Delete_todo(tid)
        elif(choice == '5'):
            break
        else:
            app.close()
            
    

if __name__ == '__main__':
    main()