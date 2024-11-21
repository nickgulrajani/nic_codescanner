# src/main.py

def process_user_input(user_input):
    # This is intentionally vulnerable for demonstration
    query = "SELECT * FROM users WHERE id = " + user_input
    return query

def secure_process_input(user_input):
    # This is the secure way
    query = "SELECT * FROM users WHERE id = %s"
    return query, [user_input]

def main():
    test_input = "1"
    result1 = process_user_input(test_input)
    result2 = secure_process_input(test_input)
    print(f"Unsafe query: {result1}")
    print(f"Safe query: {result2}")

if __name__ == "__main__":
    main()