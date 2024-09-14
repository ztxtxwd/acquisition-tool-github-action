import requests
import os
from datetime import datetime

URL = "https://juejin.cn/post/7413418434573533193"  # 替换为您要监控的网页 URL

def download_webpage():
    response = requests.get(URL)
    return response.text

def save_webpage(content):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"webpage_{timestamp}.html"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    return filename

def compare_and_save():
    new_content = download_webpage()
    
    latest_file = max([f for f in os.listdir() if f.startswith("webpage_")], default=None)
    
    if latest_file:
        with open(latest_file, "r", encoding="utf-8") as f:
            old_content = f.read()
        
        if new_content != old_content:
            new_file = save_webpage(new_content)
            print(f"Changes detected. Saved as {new_file}")
        else:
            print("No changes detected.")
    else:
        new_file = save_webpage(new_content)
        print(f"First download. Saved as {new_file}")

if __name__ == "__main__":
    compare_and_save()