from flask import Flask, request, jsonify
import mysql.connector
import os
from dotenv import load_dotenv

#  Load environment variables
load_dotenv()

app = Flask(__name__)

#  Database connection details using .env
db_config = {
    "host": os.getenv("MYSQL_HOST"),
    "user": os.getenv("MYSQL_USER"),
    "password": os.getenv("MYSQL_PASSWORD"),
    "database": os.getenv("MYSQL_DATABASE")
}

# GET endpoint to fetch sales data by date range
@app.route('/get_sales', methods=['GET'])
def get_sales():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Sales WHERE Date BETWEEN %s AND %s", (start_date, end_date))
    data = cursor.fetchall()
    
    conn.close()
    return jsonify(data)

#  POST endpoint to add a new sale
@app.route('/add_sale', methods=['POST'])
def add_sale():
    data = request.json
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO Sales (StoreID, Total_sales, Date) VALUES (%s, %s, %s)",
                   (data['StoreID'], data['Total_sales'], data['Date']))
    
    conn.commit()
    conn.close()
    return jsonify({"message": "Sale added successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
