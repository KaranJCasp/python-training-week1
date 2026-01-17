import psycopg2

def main():
    db_params = {
        'host': 'localhost',
        'database': 'books',
        'user': 'jenil',
        'password': 'Jenil@jcasp',
        'port': '5432'
    }

    conn = None
    try:
        conn = psycopg2.connect(**db_params)
        print("Connection successfull.")
        cur = conn.cursor()
        
        # --- Create a table ---
        try:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS book (
                    book_id serial PRIMARY KEY, 
                    title VARCHAR(100) NOT NULL, 
                    author VARCHAR(100),
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)
            print("Table 'book' created or already exists.")
            conn.commit() 
            
        except psycopg2.Error as e:
            print(f"I can't create or access the books database: {e}")
            if conn:
                conn.rollback()

        #---------insert data in book table-----------------------------
        data = [('as','ad'),['Ancient Mariner','Coleridge']]
        try:
            for d in data:
                cur.execute("INSERT into book(title, author) VALUES (%s, %s)", d)
            print("Table 'book'inserted data successfully.")
            conn.commit() 
            
        except psycopg2.Error as e:
            print(f"I can't insert  the books from  database: {e}")
            if conn:
                conn.rollback()

        #-----------update data in book table-------------------

        try:

            cur.execute("Update book set author='a' where author='Coleridge'")
            print("Table 'book'update data successfully.")
            conn.commit() 
            
        except psycopg2.Error as e:
            print(f"I can't update the book data from  database: {e}")
            if conn:
                conn.rollback()

        #-----------Delete data in book table-------------------
        
        try:

            cur.execute("DELETE FROM book where book_id=1")
            print("Table 'book'Deleted data in table successfully.")
            conn.commit() 
            
        except psycopg2.Error as e:
            print(f"I can't Delete the book form  database: {e}")
            if conn:
                conn.rollback()

        #-----------Retrieve data in book table-------------------
        
        try:

            cur.execute("SELECT * FROM book")
            data=cur.fetchall()
            print("Table 'book'Retrieve data successfully.", data)
            conn.commit() 
            
        except psycopg2.Error as e:
            print(f"I can't Retrieve data from database: {e}")
            if conn:
                conn.rollback()

        

    except psycopg2.Error as e:
        print(f"I am unable to connect to the database. Error: {e}")

    finally:
        if cur is not None:
            cur.close()
            print("Cursor closed.")
        if conn is not None:
            conn.close()
            print("Database connection closed.")


if __name__ == '__main__':
    main()
