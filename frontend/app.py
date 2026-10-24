import logging
import os

from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

# Database connection settings
if not os.environ.get('POSTGRES_PASSWORD'):
    raise RuntimeError('Missing required environment variable POSTGRES_PASSWORD (see .env.example).')

db_config = {
    'dbname': os.environ.get('POSTGRES_DB', 'mydatabase'),
    'user': os.environ.get('POSTGRES_USER', 'user'),
    'password': os.environ['POSTGRES_PASSWORD'],
    'host': 'db',
    'port': 5432
}

@app.route('/')
def home():
    return "Welcome to the Simple Frontend!"

@app.route('/data')
def get_data():
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor()

        # Execute a query
        cursor.execute("SELECT * FROM my_table;")
        rows = cursor.fetchall()

        # Close the connection
        cursor.close()
        conn.close()

        # Return the data as JSON
        return jsonify(rows)

    except Exception:
        app.logger.exception('Failed to fetch data from the database')
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)