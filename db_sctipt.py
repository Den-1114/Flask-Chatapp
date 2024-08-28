from sqlite3 import connect

# Function to create a new database connection
def get_db_connection():
    conn = connect('database.db')
    return conn

# Insert a new user into the users table
def insert(username, password, email):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO users (username, password, email) VALUES (?, ?, ?);', (username, password, email))
    conn.commit()
    conn.close()

# Retrieve all users from the users table
def get_users():
    conn = get_db_connection()
    cur = conn.cursor()
    users = cur.execute('SELECT * FROM users;').fetchall()
    conn.close()
    return users

# Authenticate a user based on username and password
def authenticate(username, password):
    conn = get_db_connection()
    cur = conn.cursor()
    user = cur.execute('SELECT * FROM users WHERE username = ? AND password = ?;', (username, password)).fetchone()
    conn.close()
    return user
