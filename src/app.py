# src/app.py

import os
import subprocess
import pickle
from urllib.parse import parse_qs
import sqlite3

def unsafe_sql(user_input):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    # SQL Injection vulnerability
    query = f"SELECT * FROM users WHERE username = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

def unsafe_command(user_input):
    # Command Injection vulnerability
    cmd = f"echo {user_input}"
    return subprocess.os.system(cmd)

def unsafe_deserialization(data):
    # Unsafe deserialization
    return pickle.loads(data)

def unsafe_path_handling(filename):
    # Path traversal vulnerability
    with open(f"data/{filename}", "r") as f:
        return f.read()

def unsafe_exec(code_input):
    # Code injection vulnerability
    return exec(code_input)

def process_request(query_string):
    # XSS vulnerability
    params = parse_qs(query_string)
    username = params.get('username', [''])[0]
    return f"<html><body>Hello, {username}!</body></html>"

def store_password(password):
    # Hard-coded password
    admin_password = "super_secret_123"
    return password == admin_password

def main():
    # Example usage of vulnerable functions
    user_data = {"username": "admin' OR '1'='1"}
    results = unsafe_sql(user_data["username"])
    print(results)

if __name__ == "__main__":
    main()
