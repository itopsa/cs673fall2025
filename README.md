# PostgreSQL Database Connection Demo

## Overview

This project demonstrates how to connect to a PostgreSQL database using Python and the `psycopg2` library. It includes a reusable connection function and examples of executing SQL queries.

## Files

- `database_demo.py` - Main Python script with database connection and query functionality
- `sql.ipynb` - Jupyter notebook with step-by-step database operations
- `quiz.ipynb` - Jupyter notebook with quiz questions and examples

## Prerequisites

### Software Requirements
- Python 3.7 or higher
- PostgreSQL database server
- Docker (for running PostgreSQL in a container)

### Python Dependencies
```bash
pip install psycopg2-binary
```

## Database Setup

### Using Docker (Recommended)
1. Start the PostgreSQL container:
```bash
docker start my-postgres2
```

2. Verify the container is running:
```bash
docker ps
```

### Database Configuration
The script connects to a PostgreSQL database with these default settings:
- **Host**: localhost
- **Port**: 5432
- **Database**: cs673
- **User**: postgres
- **Password**: mysecretpassword

## Usage

### Running the Script
```bash
python database_demo.py
```

### Expected Output
```
Starting main function...
Successfully connected to database 'cs673'!
Connection successful in main!

Found 12 rows in test table:
------------------------------
ID: 1, Name: John Doe
ID: 2, Name: Jane Smith
ID: 3, Name: Alice Johnson
ID: 4, Name: Bob Wilson
ID: 5, Name: Carol Brown
ID: 6, Name: David Miller
ID: 7, Name: Emma Davis
ID: 8, Name: Frank Garcia
ID: 9, Name: Grace Martinez
ID: 10, Name: Henry Anderson
ID: 11, Name: Ivy Thompson
ID: 12, Name: Jack White

Connection closed in main.
```

## Code Structure

### Functions

#### `connect_to_db(host, port, database, user, password)`
- **Purpose**: Establishes a connection to PostgreSQL database
- **Parameters**: Database connection parameters (all optional with defaults)
- **Returns**: psycopg2 connection object or None if connection fails
- **Features**: 
  - Error handling with try-except blocks
  - Informative success/error messages
  - Configurable connection parameters

#### `main()`
- **Purpose**: Demonstrates database operations and query execution
- **Features**:
  - Step-by-step database operations
  - SQL SELECT query execution
  - Result processing and display
  - Proper resource cleanup
  - Comprehensive error handling

## Database Schema

### Test Table
The script queries a table called `test` with the following structure:

```sql
CREATE TABLE test (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);
```

## Key Concepts Demonstrated

1. **Database Connection Management**
   - Establishing connections with psycopg2
   - Connection parameter configuration
   - Error handling for connection failures

2. **SQL Query Execution**
   - Creating cursor objects
   - Executing SELECT queries
   - Fetching and processing results

3. **Resource Management**
   - Proper cursor cleanup
   - Connection closure
   - Exception handling with try-except-finally

4. **Code Organization**
   - Reusable functions
   - Clear separation of concerns
   - Comprehensive documentation

## Troubleshooting

### Common Issues

1. **Connection Refused**
   - Ensure PostgreSQL container is running
   - Check if port 5432 is available
   - Verify connection parameters

2. **Authentication Failed**
   - Check username and password
   - Ensure user has access to the database

3. **Table Does Not Exist**
   - Run the table creation code from `sql.ipynb`
   - Verify you're connected to the correct database

4. **Module Not Found**
   - Install psycopg2: `pip install psycopg2-binary`
   - Check Python environment

### Debug Mode
To enable more detailed error information, you can modify the connection function to print additional debug information.

## Educational Use

This project is designed for educational purposes and demonstrates:
- Basic PostgreSQL connectivity with Python
- SQL query execution
- Error handling best practices
- Code organization and documentation
- Resource management

## Quiz Questions

The `quiz.ipynb` notebook contains programming-focused quiz questions covering:
- Database connection setup
- SQL query execution
- Error handling
- Code debugging
- Function creation

## License

This project is for educational use in CS673 course.