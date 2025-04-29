# 💱 Currency Exchange Rate Viewer (Flask + SQLite + HTML/JS)

This project is a full-stack currency exchange viewer. It allows users to select a currency pair (USD → EUR or USD → CNY) and a specific date to see exchange data such as price, open, high, low, and change percent.

It includes:

- 🔙 A Python Flask backend
- 🗃 An SQLite database
- 🌐 A frontend with HTML and vanilla JavaScript

---

## 🚀 Live Demo

Run locally at:  
`http://127.0.0.1:5000/frontend`

---

## 📁 Folder Structure

```
project-root/
├── API/
│   ├── api.py
│   └── templates/
│       └── Frontend/
│           └── index.html
├── database/
│   └── currency.db
├── README.md
```

---

## 🧠 Features

- Select currency (`usd-eur`, `usd-cny`)
- Select date (`input[type=date]`)
- View:
  - Price
  - Open
  - Close (same as price)
  - High
  - Low
  - Change (%)
- Fetches real data from an SQLite database

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/currency-api-viewer.git
cd currency-api-viewer/API
```

### 2. Create a Virtual Environment (optional but recommended)

```bash
python3 -m venv .venv
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate   # Windows
```

### 3. Install Dependencies

```bash
pip install flask flask-cors
```

### 4. Run the Server

```bash
python api.py
```

Now the backend is running at:  
`http://127.0.0.1:5000`

### 5. Open the Frontend

In your browser:  
`http://127.0.0.1:5000/frontend`

---

## 🐍 `api.py` - Backend Overview

- Flask app with 4 routes:
  - `/` – API welcome message
  - `/usd-cny` – data from USD to CNY table
  - `/usd-eur` – data from USD to EUR table
  - `/frontend` – serves the HTML interface
- SQLite is used as a local embedded database
- CORS is enabled for frontend/backend communication

---

## 🌐 Frontend (HTML + JS)

### How it works:

- User selects a currency + date
- JS converts `YYYY-MM-DD` → `M/D/YY`
- Makes a GET request:  
  `http://127.0.0.1:5000/usd-eur?date=4/29/25`
- Displays a result table with values if found

---

## 💾 Example Data Schema (`currency.db`)

Your SQLite tables should have columns like:

- `Date` — stored as `M/D/YY` (e.g., `4/29/25`)
- `Price`
- `Open`
- `High`
- `Low`
- `Change_Percent`

Table names:

- `"exchange_rates_usd-eur"`
- `"exchange_rates_usd_cny"`

---

## 📦 Example API Call

```http
GET /usd-eur?date=4/29/25

Response:
[
  {
    "Date": "4/29/25",
    "Price": "0.8772",
    "Open": "0.8765",
    "High": "0.8792",
    "Low": "0.8757",
    "Change_Percent": "0.07"
  }
]
```

---

## 📌 To-Do & Extensions

- [ ] Add monthly summaries (min, max, avg)
- [ ] Export table to CSV
- [ ] Add chart view using Chart.js
- [ ] Style frontend with TailwindCSS or Bootstrap

---

## 📜 License

MIT License

---

## 🙋‍♂️ Author

**Pavel**  
Want help building or expanding your app? Feel free to contact me or fork this repo!