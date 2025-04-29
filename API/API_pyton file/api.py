from flask import Flask, jsonify, render_template
from flask_cors import CORS
import sqlite3
import os

app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, '..', 'database', 'currency.db')

def get_data_from_table(table_name):
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

@app.route('/')
def home():
    return jsonify({"message": "Currency API Ready", "routes": ["/usd-cny", "/usd-eur", "/frontend"]})

@app.route('/usd-cny')
def usd_cny():
    return jsonify(get_data_from_table('exchange_rates_usd_cny'))

@app.route('/usd-eur')
def usd_eur():
    return jsonify(get_data_from_table('"exchange_rates_usd-eur"'))

@app.route('/frontend')
def frontend():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)