import json
import os

DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'database', 'companies.json')

def check_pending():
    if not os.path.exists(DB_PATH):
        print("Database not found.")
        return
    
    with open(DB_PATH, 'r', encoding='utf-8') as f:
        db = json.load(f)
    
    pending = [c for c in db if c.get('analysis_pending')]
    
    if pending:
        print(f"--- {len(pending)} PENDING ANALYSIS REQUESTS ---")
        for p in pending:
            print(f"ID: {p['id']} | Name: {p['name']} | Authorized Insta: {p.get('insta_handle')} | User: {p.get('username')}")
    else:
        print("No pending analysis requests.")

if __name__ == "__main__":
    check_pending()
