# tests/test_security.py
import pytest
import pickle
from src.app import (
    unsafe_sql,
    unsafe_command,
    unsafe_deserialization,
    unsafe_path_handling,
    unsafe_exec,
    process_request,
    store_password
)

def test_unsafe_sql():
    user_input = "admin' OR '1'='1"
    try:
        result = unsafe_sql(user_input)
        print(f"SQL Query Result: {result}")
    except Exception as e:
        print(f"SQL Error: {e}")

def test_unsafe_command():
    user_input = "hello; ls -la"
    try:
        result = unsafe_command(user_input)
        print(f"Command Result: {result}")
    except Exception as e:
        print(f"Command Error: {e}")

def test_unsafe_deserialization():
    malicious_pickle = pickle.dumps({"user": "admin"})
    try:
        result = unsafe_deserialization(malicious_pickle)
        print(f"Deserialization Result: {result}")
    except Exception as e:
        print(f"Deserialization Error: {e}")

def test_unsafe_path():
    filename = "../../../etc/passwd"
    try:
        result = unsafe_path_handling(filename)
        print(f"File Content: {result}")
    except Exception as e:
        print(f"File Error: {e}")

def test_process_request():
    query_string = "username=<script>alert('xss')</script>"
    result = process_request(query_string)
    print(f"XSS Result: {result}")

def test_password_storage():
    password = "super_secret_123"
    result = store_password(password)
    print(f"Password Check: {result}")