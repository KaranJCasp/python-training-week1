Use json.dumps() to convert a Python dictionary to a formatted JSON string. 

import json

data = {
    "name": "Alice",
    "age": 30,
    "hobbies": ["reading", "chess", "hiking"],
    "address": {
        "street": "123 Main St",
        "city": "Wonderland"
    }
}

# Convert the Python dictionary to a JSON string with 4 spaces of indentation
json_string = json.dumps(data, indent=4)

print(json_string)


linear data structure 

stack (lifo):

stack = []
stack.append('A')
stack.append('B')
stack.append('C')
print("Stack:", stack)
popped_element = stack.pop()
print("Popped element:", popped_element)
print("Stack after pop:", stack)

Queues (First-In, First-Out: FIFO) 
A queue follows the First-In, First-Out (FIFO) principle, like people waiting in line. 

from collections import deque
queue = deque()
queue.append('Task1')
queue.append('Task2')
queue.append('Task3')
print("Queue:", queue)
dequeued_element = queue.popleft()
print("Dequeued element:", dequeued_element)
print("Queue after dequeue:", queue)


How to insall Pgadmin

note : "Create the repository configuration file" means creating a text file on your computer that tells your package manager (like yum, dnf, apt) or software application where to find, download, and verify software packages.  


#
# Setup the repository
#

# Install the public key for the repository (if not done previously):
curl -fsS https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo gpg --dearmor -o /usr/share/keyrings/packages-pgadmin-org.gpg

# Create the repository configuration file:
sudo sh -c 'echo "deb [signed-by=/usr/share/keyrings/packages-pgadmin-org.gpg] https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/$(lsb_release -cs) pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list && apt update'

#
# Install pgAdmin
#

# Install for both desktop and web modes:
sudo apt install pgadmin4

# Install for desktop mode only:
sudo apt install pgadmin4-desktop

# Install for web mode only: 
sudo apt install pgadmin4-web 

# Configure the webserver, if you installed pgadmin4-web:
sudo /usr/pgadmin4/bin/setup-web.sh


===================================================================================

1 . import sqlite library 
2. make establish the conncetion 
3. Create a Cursor Object  = The cursor acts as an intermediary for executing SQL commands.

4. which query you perform that write first and using the 
   cursor  execute the command - cursor.execute(

5. Commit Changes: For any data manipulation (INSERT, UPDATE, DELETE), you must commit the changes to the database using the connection object's commit() method.
python
conn.commit()


