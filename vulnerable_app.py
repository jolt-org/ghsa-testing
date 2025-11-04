"""
A simple vulnerable Python application for testing security scanners.
Contains SQL injection vulnerability.
"""

import sqlite3

def get_user_by_username(username):
    """Fetch user from database - VULNERABLE to SQL injection"""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # VULNERABILITY: SQL Injection - user input directly concatenated into query
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    
    result = cursor.fetchone()
    conn.close()
    return result

def main():
    # Example usage
    user_input = input("Enter username: ")
    user = get_user_by_username(user_input)
    
    if user:
        print(f"User found: {user}")
    else:
        print("User not found")

if __name__ == "__main__":
    main()
