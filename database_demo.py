#!/usr/bin/env python3
"""
PostgreSQL Database Connection Demo Script

This script demonstrates:
1. Connecting to a PostgreSQL database using psycopg2
2. Creating a reusable connection function
3. Executing SQL SELECT queries
4. Processing and displaying query results
5. Proper resource cleanup and error handling

Author: CS673 Course
"""

import psycopg2


def connect_to_db(host="localhost", port=5432, database="cs673", user="postgres", password="mysecretpassword"):
    """
    Connect to PostgreSQL database
    
    Parameters:
    host (str): Database host (default: localhost)
    port (int): Database port (default: 5432)
    database (str): Database name (default: cs673)
    user (str): Database user (default: postgres)
    password (str): Database password (default: mysecretpassword)
    
    Returns:
    connection: psycopg2 connection object or None if connection fails
    """
    try:
        conn = psycopg2.connect(
            host=host,
            port=port,
            database=database,
            user=user,
            password=password
        )
        print(f"Successfully connected to database '{database}'!")
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None


def main():
    """
    Main entrypoint function that demonstrates:
    1. Database connection using our custom function
    2. Executing SQL SELECT queries
    3. Processing query results
    4. Proper resource cleanup
    """
    print("Starting main function...")
    
    # Step 1: Establish database connection using our reusable function
    conn = connect_to_db()
    
    # Step 2: Check if connection was successful
    if conn:
        print("Connection successful in main!")
        
        # Step 3: Perform database operations with error handling
        # The try block protects database operations from crashing the program
        # If any error occurs (connection issues, SQL errors, etc.), 
        # the except block will catch it and display a helpful error message
        try:
            # Create a cursor object to execute SQL commands
            # A cursor is like a pointer that allows us to execute queries
            cursor = conn.cursor()
            
            # Step 4: Execute a SELECT query to retrieve all data from test table
            # SELECT * means "get all columns" from the test table
            cursor.execute("SELECT * FROM test;")
            
            # Step 5: Fetch all results from the query
            # fetchall() returns a list of tuples, where each tuple is a row
            results = cursor.fetchall()
            
            # Step 6: Display the results in a formatted way
            print(f"\nFound {len(results)} rows in test table:")
            print("-" * 30)
            
            # Loop through each row and display the data
            # row[0] is the first column (id), row[1] is the second column (name)
            for row in results:
                print(f"ID: {row[0]}, Name: {row[1]}")
            
            # Step 7: Close the cursor to free up resources
            cursor.close()
            
        # The except block catches any errors that occur in the try block
        # Exception as e captures the error details for display
        # This prevents the program from crashing and provides helpful error messages
        except Exception as e:
            # Handle any errors that occur during database operations
            print(f"Error during database operations: {e}")
        
        # The finally block ALWAYS executes, whether there was an error or not
        # This is crucial for cleanup operations like closing database connections
        # It ensures resources are properly released even if something goes wrong
        finally:
            # Step 8: Always close the database connection
            # This ensures we don't leave connections open
            conn.close()
            print("\nConnection closed in main.")
    else:
        # Handle case where connection failed
        print("Failed to connect in main.")


# This block ensures main() only runs when the script is executed directly
# It prevents main() from running when the script is imported as a module
# This is a Python best practice for creating reusable scripts
if __name__ == "__main__":
    main()
