from flask import Flask, request, jsonify
import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Database connection
def connect_db():
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "127.0.0.1"),
        user=os.getenv("MYSQL_USER", "root"),
        password=os.getenv("MYSQL_PASSWORD", ""),
        database=os.getenv("MYSQL_DATABASE", ""),
        port=int(os.getenv("MYSQL_PORT", 3306))
    )

# GET sales by date range
@app.route('/get_sales', methods=['GET'])
def get_sales():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    conn = connect_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Sales WHERE Date BETWEEN %s AND %s", (start_date, end_date))
    data = cursor.fetchall()
    conn.close()
    
    return jsonify(data)

# POST add a new sale
@app.route('/add_sale', methods=['POST'])
def add_sale():
    data = request.json

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Sales (StoreID, Total_sales, Date) VALUES (%s, %s, %s)",
                   (data['StoreID'], data['Total_sales'], data['Date']))
    
    conn.commit()
    conn.close()
    
    return jsonify({"message": "Sale added successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
