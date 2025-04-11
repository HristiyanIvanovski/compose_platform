from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

# Database connection settings
db_config = {
    'dbname': 'mydatabase',
    'user': 'user',
    'password': 'password',
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

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)