import requests
import os
from datetime import datetime

URL = "https://juejin.cn/post/7413418434573533193"  # 替换为您要监控的网页 URL
SAVE_DIR = "webpage_archives"  # 保存网页的目录

def download_webpage():
    response = requests.get(URL)
    print(response.text)
    return response.text

def save_webpage(content):
    if not os.path.exists(SAVE_DIR):
        os.makedirs(SAVE_DIR)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"webpage_{timestamp}.html"
    filepath = os.path.join(SAVE_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    return filename

def compare_and_save():
    new_content = download_webpage()
    
    files = [f for f in os.listdir(SAVE_DIR) if f.startswith("webpage_")]
    latest_file = max(files, default=None) if files else None
    
    if latest_file:
        with open(os.path.join(SAVE_DIR, latest_file), "r", encoding="utf-8") as f:
            old_content = f.read()
        
        if new_content != old_content:
            new_file = save_webpage(new_content)
            print(f"检测到变化。已保存为 {new_file}")
        else:
            print("未检测到变化。")
    else:
        new_file = save_webpage(new_content)
        print(f"首次下载。已保存为 {new_file}")

if __name__ == "__main__":
    compare_and_save()