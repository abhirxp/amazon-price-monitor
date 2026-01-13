# amazon-price-monitor

# 🛒 Amazon Price Monitor & Logger

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Library](https://img.shields.io/badge/Library-BeautifulSoup4-green)
![Focus](https://img.shields.io/badge/Focus-Automation-orange)

## 📋 Project Overview
A robust Python automation script designed to track product prices on Amazon. This tool assists e-commerce analysts and shoppers by automating the manual process of checking URLs, logging historical price data into CSV format for analysis.

**Business Value:**
* **Time Saving:** Eliminates the need for manual daily checks.
* **Data Aggregation:** Builds a dataset over time to visualize price trends and inflation.
* **Scalable:** Can handle multiple products simultaneously via a configuration file.

## ⚙️ Key Features
* **Anti-Bot Evasion:** Implements `User-Agent` rotation and randomized sleep intervals to mimic human behavior and avoid IP bans.
* **External Configuration:** Uses `config.json` to manage URLs, allowing non-technical users to update product lists without touching the code.
* **Resilient Error Handling:** Detects "Out of Stock" items, Captcha blocks, and DOM changes, logging them without crashing the script.
* **Structured Logging:** Automatically appends data to a timestamped CSV file for easy import into Excel or Tableau.

## 🛠️ Technical Implementation
* **Requests:** For HTTP session handling.
* **BeautifulSoup4:** For parsing HTML and DOM traversal.
* **JSON/CSV Modules:** For data persistence and configuration management.

## 🚀 How to Run

1. **Clone the repository**
   ```bash
   git clone [https://github.com/abhirxp/amazon-price-monitor.git](https://github.com/abhirxp/amazon-price-monitor.git)
   cd amazon-price-monitor

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. Configure Products
   * Open config.json
   * Add the Name and URL of the products you want to track.

4. Run the Script
   ```bash
   python main.py
   ```
5. The script generates a price_history.csv file automatically.

## 🔮Future Improvements
[ ] Add Email/Telegram alerts when price drops below a threshold.

[ ] Integrate SQLite database for long-term storage.

[ ] Build a simple Streamlit dashboard to visualize the price history.

Created by [abhirxp] - Open for Freelance Automation Projects.
