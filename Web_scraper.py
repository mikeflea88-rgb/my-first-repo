import requests
from bs4 import BeautifulSoup
import time

print("=== CEO SMART SCRAPER v2.0 ===")
print("This one bypasses basic blocks\n")

url = input("Paste product URL: ")

try:
    # Better headers - looks like Chrome on Android
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
    }
    
    print("Scraping... please wait 3 seconds")
    time.sleep(3) # wait so we don't look like a robot
    
    page = requests.get(url, headers=headers, timeout=10)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    # Try 3 different ways to find price because every site is different
    price = soup.find('span', class_='-b -ltr -tal -fs24') # Jumia price class
    if not price:
        price = soup.find('span', class_='price')
    if not price:
        price = soup.find('div', class_='price')
    
    title = soup.find('h1')
    
    print(f"\n--- RESULT ---")
    print(f"Product: {title.get_text().strip() if title else 'Not Found'}")
    print(f"Price: {price.get_text().strip() if price else 'Not Found'}")
    print(f"Link: {url}")
    print("----------------")

except Exception as e:
    print(f"Error: {e}")
    print("Tip: Try a different product or site. Some sites need VPN")
