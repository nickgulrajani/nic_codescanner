# src/vulnerable.py
import sqlite3
import os

def bad_sql_query(user_input):
    """Deliberately vulnerable SQL query"""
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    # WARNING: This is vulnerable to SQL injection
    query = "SELECT * FROM users WHERE name = '" + user_input + "'"
    cursor.execute(query)
    return cursor.fetchall()

def bad_file_access(filename):
    """Deliberately vulnerable file access"""
    # WARNING: This is vulnerable to path traversal
    return open(os.path.join("data", filename)).read()

def bad_command_execution(user_input):
    """Deliberately vulnerable command execution"""
    # WARNING: This is vulnerable to command injection
    return os.system(f"echo {user_input}")

if __name__ == "__main__":
    # Example usage
    user_input = "admin' OR '1'='1"
    result = bad_sql_query(user_input)
    print(result)

