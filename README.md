Data Engineering Intern Project
A simple Flask API to manage sales data.

INSTALL DEPENDENCIES
pip install -r requirements.txt

MODIFY YOUR .ENV FILE!
MYSQL_USER=root
MYSQL_PASSWORD=YOUR_PASSWORD
MYSQL_HOST=localhost
MYSQL_DATABASE=StoreData

RUN API
python app.py

HOW TO USE  WHEN ADDING A NEW SALE
curl -X POST http://127.0.0.1:5000/add_sale \
     -H "Content-Type: application/json" \
     -d '{"StoreID": 1, "Total_sales": 500.75, "Date": "2025-03-09"}'
     PUT THIS INTO THE TERMENAL TO ADD SALE


GET A SALES DATE RANGE!
curl "http://127.0.0.1:5000/get_sales?start_date=2025-03-01&end_date=2025-03-31"
MODIFY THE START DATE AND END DATE TO GET THE VALUES