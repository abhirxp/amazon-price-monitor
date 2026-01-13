import requests
from bs4 import BeautifulSoup
import re
import time
import random
import csv
import datetime
import json
import os

# --- CONSTANTS & CONFIGURATION ---
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
]


def load_config(filename="config.json"):
    """Loads target products from an external JSON file."""
    if not os.path.exists(filename):
        print(f"[ERROR] Configuration file '{filename}' not found.")
        return []
    with open(filename, 'r') as f:
        return json.load(f)


# --- SCRAPER LOGIC ---
def get_amazon_price(url):
    """
    Fetches the price of a product.
    Returns: Float (price), String (error message), or None.
    """
    # Mimic human behavior: Random delay and Random User-Agent
    delay = random.uniform(2, 5)
    time.sleep(delay)

    current_headers = {
        "User-Agent": random.choice(USER_AGENTS),
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://www.google.com/"
    }

    try:
        response = requests.get(url, headers=current_headers)
        soup = BeautifulSoup(response.content, "html.parser")

        # Anti-Bot Check
        if "Enter the characters you see below" in soup.text:
            return "BLOCKED_BY_CAPTCHA"

        # Availability Check
        availability = soup.find("div", {"id": "availability"})
        if availability and "Currently unavailable" in availability.get_text():
            return "OUT_OF_STOCK"

        # Price Extraction logic
        price_element = soup.find("span", {"class": "a-price-whole"})
        if not price_element:
            price_element = soup.find("span", {"class": "a-offscreen"})

        if price_element:
            raw_text = price_element.get_text()
            # Remove currency symbols and commas
            numeric_price = re.sub(r'[^\d.]', '', raw_text)
            return float(numeric_price)

        return "PRICE_NOT_FOUND_IN_DOM"

    except Exception as e:
        return f"ERROR: {str(e)}"


# --- DATA PERSISTENCE ---
def log_data_to_csv(product_name, price, link):
    filename = "price_history.csv"
    today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        file_exists = os.path.isfile(filename)
        with open(filename, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # Write header only if file is new
            if not file_exists:
                writer.writerow(["Timestamp", "Product Name", "Price", "Link"])

            writer.writerow([today, product_name, price, link])
            print(f"   [Saved] {product_name}: {price}")

    except Exception as e:
        print(f"   [File Error] Could not save data: {e}")


# --- MAIN EXECUTION ---
if __name__ == "__main__":
    print("--- Amazon Price Monitor Started ---")

    products = load_config()

    if not products:
        print("No products found in config.json. Exiting.")
    else:
        print(f"Tracking {len(products)} items...")

        for item in products:
            print(f"\nProcessing: {item['name']}")
            result = get_amazon_price(item['url'])

            if isinstance(result, float):
                log_data_to_csv(item['name'], result, item['url'])
            else:
                print(f"   [Skipped] Status: {result}")

    print("\n--- Job Complete ---")