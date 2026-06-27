import json
import os
from scraper import scrape

state = "sale_end.json"

def save_data():
    with open(state, 'w', encoding='utf-8') as f:
        json.dump(scrape(), f, indent=4, ensure_ascii=False)

def load_data():
    if not os.path.exists(state):
        return None
    with open(state, 'r', encoding='utf-8') as f:
        return json.load(f)
